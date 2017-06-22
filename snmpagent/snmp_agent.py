import os

import snmp_engine
from parsers import config_parser
from pysnmp import debug
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.carrier.asyncore.dispatch import AsyncoreDispatcher
from pysnmp.entity import config

debug.setLogger(debug.Debug('all'))


class SNMPAgent(object):
    def __init__(self, config_file, auth_config_file):
        self.config_file = config_file
        self.auth_config_file = auth_config_file
        self._parse_config()
        self._parse_auth_config()

    def _parse_config(self):
        self.agent_config = config_parser.SNMPAgentConfig(self.config_file)
        self.default_config = self.agent_config.sections['default']
        self.unity_config = self.agent_config.get_sections_by_type('unity')

    def _parse_auth_config(self):
        self.auth_config = config_parser.AuthConfig(self.auth_config_file)

    def _add_users(self, engine):
        # snmpget -v3 -u usr-md5-des -l authPriv -A authkey1 -X privkey1 192.168.56.1 1.3.6.1.4.1.1139.103.2.2.0
        # snmpget -v3 -u usr-sha-none -l authNoPriv -a SHA -A authkey1 192.168.56.1 1.3.6.1.4.1.1139.103.2.2.0
        # snmpget -v3 -u usr-sha-aes128 -l authPriv -a SHA -A authkey1 -x AES -X privkey1 192.168.56.1 1.3.6.1.4.1.1139.103.2.2.0
        # snmpwalk -v3 -u usr-md5-des -l authPriv -A authkey1 -X privkey1 192.168.56.1 .1.3.6
        # snmpwalk -v3 -u usr-sha-none -l authNoPriv -a SHA -A authkey1 192.168.56.1 .1.3.6
        # snmpwalk -v3 -u usr-sha-aes128 -l authPriv -a SHA -A authkey1 -x AES -X privkey1 192.168.56.1 .1.3.6

        auth_protocols = {'md5': config.usmHMACMD5AuthProtocol,
                          'sha': config.usmHMACSHAAuthProtocol,
                          # 'noauth': config.usmNoAuthProtocol
                          }
        priv_protocols = {'des': config.usmDESPrivProtocol,
                          'aes': config.usmAesCfb128Protocol,
                          # 'nopriv': config.usmNoPrivProtocol
                          }

        # TODO: Need to define read_sub_tree in conf file?
        read_sub_tree = (1, 3, 6)

        for user in self.auth_config.users:
            if user.model == 'snmpv3':
                # TODO: failed to add admin
                # TODO: failed to add "SNMPv3  usr-sha-none  -  authNoPriv  sha  authkey1  -  -"
                auth_proto = auth_protocols.get(user.auth_proto, None)
                priv_proto = priv_protocols.get(user.priv_proto, None)
                engine.addV3User(user.security_name, auth_proto, user.auth_key, priv_proto, user.priv_key)
                engine.addVacmUser(3, user.security_name, user.security_level, read_sub_tree, read_sub_tree)

            if user.model == 'snmpv2c':
                engine.addV1System(user.security_name, user.community)
                engine.addVacmUser(2, user.security_name, 'noAuthNoPriv', read_sub_tree, read_sub_tree)

    def run(self):
        self.transport_dispatcher = AsyncoreDispatcher()
        self.transport_dispatcher.registerRoutingCbFun(lambda td, t, d: td)

        for idx, unity in enumerate(self.unity_config):
            transport_domain = udp.domainName + (idx,)
            engine = snmp_engine.SNMPEngine()
            engine.registerTransportDispatcher(self.transport_dispatcher, transport_domain)

            port = int(unity.port)
            engine.addTransport(self.default_config.ip, port, idx)

            self._add_users(engine)

            engine.create_managed_object_instance()
            engine.register_snmp_application()

        self.transport_dispatcher.jobStarted(1)

        # Run I/O dispatcher which would receive queries and send responses
        try:
            self.transport_dispatcher.runDispatcher()
        except:
            self.transport_dispatcher.closeDispatcher()
            raise


if __name__ == '__main__':
    config_file = os.path.abspath('conf/snmpagent.conf')
    auth_config_file = os.path.abspath('conf/access.conf')
    agent = SNMPAgent(config_file, auth_config_file)
    agent.run()
