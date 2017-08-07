from pysnmp.carrier.asyncore import dispatch
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.smi import builder as snmp_builder
from snmpagent import clients, enums, factory, mib_parser
from snmpagent import config as snmp_config

READ_SUB_TREE = (1, 3, 6, 1, 4, 1, 1139, 103)
WRITE_SUB_TREE = READ_SUB_TREE


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
            return clients.UnityClient.get_unity_client(
                client_name, self.array_config.mgmt_ip,
                self.array_config.user, self.array_config.password)
        except:
            # TODO: log
            return None

    def create_managed_objects(self):
        builder = self.context.getMibInstrum().getMibBuilder()
        # Add Unity-MIB.py to mib source dir
        builder.setMibSources(
            snmp_builder.DirMibSource(os.path.abspath('./mibs/')),
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

        builder.exportSymbols('Unity-MIB', *instances)

    def register_cmd_responders(self):
        """Registers command responders."""
        cmdrsp.GetCommandResponder(self.engine, self.context)
        cmdrsp.SetCommandResponder(self.engine, self.context)
        cmdrsp.NextCommandResponder(self.engine, self.context)
        cmdrsp.BulkCommandResponder(self.engine, self.context)


class SNMPAgent(object):
    def __init__(self, agent_conf_file, access_conf_file):
        self.agent_config = snmp_config.AgentConfig(agent_conf_file).entries
        self.access_config = snmp_config.UserConfig(access_conf_file).entries
        self.transport_dispatcher = dispatch.AsyncoreDispatcher()

    def run(self):
        self.transport_dispatcher.registerRoutingCbFun(lambda td, t, d: td)
        for index, array_name in enumerate(self.agent_config):
            SNMPEngine(self.agent_config[array_name], self.access_config,
                       engine_id=index,
                       transport_dispatcher=self.transport_dispatcher)

        self.transport_dispatcher.jobStarted(1)

        # Run I/O dispatcher which would receive queries and send responses
        try:
            self.transport_dispatcher.runDispatcher()
        except:
            self.transport_dispatcher.closeDispatcher()
            raise


if __name__ == '__main__':
    from pysnmp import debug

    # debug.setLogger(debug.Debug('all'))
    import os

    config_file = os.path.abspath('configs/agent.conf')
    auth_config_file = os.path.abspath('configs/access.conf')
    agent = SNMPAgent(config_file, auth_config_file)
    agent.run()
