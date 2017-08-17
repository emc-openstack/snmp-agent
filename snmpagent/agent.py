import logging
import os
import threading

from pysnmp.carrier.asyncore import dispatch
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.smi import builder as snmp_builder
from snmpagent import clients, enums, factory, mib_parser
from snmpagent import config as snmp_config
from snmpagent import utils

READ_SUB_TREE = (1, 3, 6, 1, 4, 1, 1139, 103)
WRITE_SUB_TREE = READ_SUB_TREE

LOG = logging.getLogger(__name__)


class SNMPEngine(object):
    def __init__(self, array_config, access_config, engine_id=None,
                 transport_dispatcher=None):
        self.array_config = array_config
        self.access_config = access_config
        self.port = (int(array_config.agent_port) if array_config.agent_port
                     else 161)
        self.ip = (array_config.agent_ip if array_config.agent_ip
                   else '0.0.0.0')
        self.engine_id = engine_id
        self.transport_dispatcher = (dispatch.AsyncoreDispatcher()
                                     if transport_dispatcher is None
                                     else transport_dispatcher)

        self.engine = engine.SnmpEngine()
        self.context = context.SnmpContext(self.engine)

        self.setup_transport()
        self.setup_access()
        self.engine.unity_client = self.connect_backend_device()
        self.engine.parent = self
        self.create_managed_objects()
        self.register_cmd_responders()
        self.enable_observer()

    def setup_transport(self):
        transport_domain = udp.domainName + (self.engine_id,)
        self.engine.registerTransportDispatcher(self.transport_dispatcher,
                                                transport_domain)
        config.addTransport(self.engine, transport_domain,
                            udp.UdpTransport().openServerMode(
                                (self.ip, self.port)))

    def setup_access(self):
        auth_mapping = {enums.AuthProtocol.MD5: config.usmHMACMD5AuthProtocol,
                        enums.AuthProtocol.SHA: config.usmHMACSHAAuthProtocol,
                        None: config.usmNoAuthProtocol}
        priv_mapping = {enums.PrivProtocol.DES: config.usmDESPrivProtocol,
                        enums.PrivProtocol.AES: config.usmAesCfb128Protocol,
                        None: config.usmNoPrivProtocol}

        for name, obj in self.access_config.items():
            if obj.mode == enums.UserVersion.V3:
                config.addV3User(self.engine, name,
                                 auth_mapping[obj.auth_protocol],
                                 obj.auth_key.raw,
                                 priv_mapping[obj.priv_protocol],
                                 obj.priv_key.raw)
                config.addVacmUser(self.engine, 3, name,
                                   obj.security_level.value, READ_SUB_TREE,
                                   WRITE_SUB_TREE)
            else:
                config.addV1System(self.engine, name, obj.community.value)
                config.addVacmUser(self.engine, 2, name,
                                   enums.SecurityLevel.NO_AUTH_NO_PRIV.value,
                                   READ_SUB_TREE, WRITE_SUB_TREE)

    def connect_backend_device(self):
        client_name = '{ip}_{port}'.format(ip=self.array_config.mgmt_ip,
                                           port=self.array_config.agent_port)
        try:
            LOG.debug('Connecting to unity: {}, agent port: {}'.format(
                self.array_config.mgmt_ip, self.port))
            cache_interval = (int(self.array_config.cache_interval)
                              if self.array_config.cache_interval else 30)
            return clients.UnityClient.get_unity_client(
                client_name, self.array_config.mgmt_ip,
                self.array_config.user, self.array_config.password,
                cache_interval=cache_interval)
        except Exception as ex:
            LOG.warning(
                'Failed to reconnect unity: {}, agent port: {}, '
                'reason: {}'.format(
                    self.array_config.mgmt_ip, self.port, ex))
            return None

    def create_managed_objects(self):
        builder = self.context.getMibInstrum().getMibBuilder()
        # Add Unity-MIB.py to mib source dir
        mib_dir_path = os.path.join(os.path.dirname(__file__), 'mibs')
        builder.setMibSources(
            snmp_builder.DirMibSource(mib_dir_path),
            *builder.getMibSources())

        mib_scalar, mib_table_column, mib_table_row, mib_scalar_instance = (
            builder.importSymbols('SNMPv2-SMI', 'MibScalar', 'MibTableColumn',
                                  'MibTableRow', 'MibScalarInstance'))

        module_name = "Unity-MIB"
        instances = []
        table_rows = []

        mib_symbols = [item[0]
                       for item in mib_parser.get_mib_symbols(module_name)]

        mib_objects = builder.importSymbols(module_name, *mib_symbols)

        for item in mib_objects:
            if isinstance(item, mib_table_row):
                table_rows.append(item)

        for item in mib_objects:
            class_name = item.label[:1].upper() + item.label[1:]

            try:
                mod = __import__("unity_impl." + class_name,
                                 fromlist=[item.label])
            except ImportError:
                continue

            if isinstance(item, mib_table_column):
                entry = None
                for row in table_rows:
                    if row.getName() == item.getName()[:-1]:
                        entry = row

                scalar_instance_clz = factory.ScalarInstanceFactory.build(
                    class_name, base_class=mib_scalar_instance,
                    impl_class=getattr(mod, class_name))

                column_instance_clz = factory.TableColumnInstanceFactory.build(
                    class_name, base_class=mib_table_column,
                    proto_inst=scalar_instance_clz, entry=entry,
                    impl_class=getattr(mod, class_name + "Column"))
                instances.append(column_instance_clz(item.name, item.syntax))

            elif isinstance(item, mib_scalar):
                scalar_instance_clz = factory.ScalarInstanceFactory.build(
                    class_name, base_class=mib_scalar_instance,
                    impl_class=getattr(mod, class_name))
                instances.append(scalar_instance_clz(item.name, (0,),
                                                     item.syntax))
        builder.exportSymbols('Exported-Unity-MIB', *instances)

    def register_cmd_responders(self):
        """Registers command responders."""
        cmdrsp.GetCommandResponder(self.engine, self.context)
        cmdrsp.SetCommandResponder(self.engine, self.context)
        cmdrsp.NextCommandResponder(self.engine, self.context)
        cmdrsp.BulkCommandResponder(self.engine, self.context)

    def enable_observer(self):
        self.engine.observer.registerObserver(
            self.request_observer,
            'rfc3412.receiveMessage:request',
            'rfc3412.returnResponsePdu'
        )

    def request_observer(self, engine, execpoint, variables, cb_ctx):
        LOG.debug('Execution point: %s' % execpoint)
        LOG.debug('* transportDomain: %s' % '.'.join(
            [str(x) for x in variables['transportDomain']]))
        LOG.debug('* transportAddress: %s (local %s)' % (
            '@'.join([str(x) for x in variables['transportAddress']]),
            '@'.join([str(x) for x in
                      variables['transportAddress'].getLocalAddress()])))
        LOG.debug('* securityModel: %s' % variables['securityModel'])
        LOG.debug('* securityName: %s' % variables['securityName'])
        LOG.debug('* securityLevel: %s' % variables['securityLevel'])
        LOG.debug('* contextEngineId: %s' % variables[
            'contextEngineId'].prettyPrint())
        LOG.debug('* contextName: %s' % variables['contextName'].prettyPrint())
        LOG.debug('* PDU: %s' % variables['pdu'].prettyPrint())


class SNMPAgent(object):
    def __init__(self, agent_conf_file, access_conf_file):
        self.agent_entries = snmp_config.AgentConfig(agent_conf_file).entries
        self.access_entries = snmp_config.UserConfig(access_conf_file).entries
        utils.setup_log(
            log_file_path=self.agent_entries.default_section.log_file,
            level=self.agent_entries.default_section.log_level,
            max_bytes=self.agent_entries.default_section.log_file_maxbytes,
            max_file_count=self.agent_entries.default_section.log_file_count)
        self.transport_dispatcher = None

    def run_instance(self, agent_config, access_config, engine_id):
        transport_dispatcher = dispatch.AsyncoreDispatcher()
        transport_dispatcher.registerRoutingCbFun(lambda td, t, d: td)
        SNMPEngine(agent_config, access_config, engine_id,
                   transport_dispatcher)
        transport_dispatcher.jobStarted(1)

        # Run I/O dispatcher which would receive queries and send responses
        try:
            transport_dispatcher.runDispatcher()
        except Exception as ex:
            LOG.error("Failed to run dispatcher, error: {}".format(ex))
            transport_dispatcher.closeDispatcher()
            raise

    def run(self):
        """Starts the SNMP engine in multi-thread mode."""
        for index, array_name in enumerate(self.agent_entries):
            t = threading.Thread(target=self.run_instance,
                                 args=(
                                     self.agent_entries[array_name],
                                     self.access_entries, index))
            t.start()
            LOG.info("Started engine for array config [{}]".format(array_name))


if __name__ == '__main__':
    config_file = os.path.abspath('configs/agent.conf')
    auth_config_file = os.path.abspath('configs/access.conf')
    agent = SNMPAgent(config_file, auth_config_file)
    agent.run()
