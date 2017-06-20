import os

from pysnmp import debug
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.carrier.asyncore.dispatch import AsyncoreDispatcher
from pysnmp.entity import config

import snmp_engine
from parsers import config_parser

debug.setLogger(debug.Debug('all'))


class SNMPAgent(object):
    def __init__(self, config_file):
        self.config_file = config_file

    def parse_config(self):
        self.agent_config = config_parser.SNMPAgentConfig(self.config_file)
        self.auth_config = self.agent_config.get_sections_by_type('auth')
        self.unity_config = self.agent_config.get_sections_by_type('unity')

    def add_users(self, engine):
        # snmpget -v3 -u usr-md5-des -l authPriv -A authkey1 -X privkey1 192.168.56.1 1.3.6.1.4.1.1139.103.2.2.0
        # snmpget -v3 -u usr-sha-none -l authNoPriv -a SHA -A authkey1 192.168.56.1 1.3.6.1.4.1.1139.103.2.2.0
        # snmpget -v3 -u usr-sha-aes128 -l authPriv -a SHA -A authkey1 -x AES -X privkey1 192.168.56.1 1.3.6.1.4.1.1139.103.2.2.0
        # snmpwalk -v3 -u usr-md5-des -l authPriv -A authkey1 -X privkey1 localhost .1.3.6
        # snmpwalk -v3 -u usr-sha-none -l authNoPriv -a SHA -A authkey1 localhost .1.3.6
        # snmpwalk -v3 -u usr-sha-aes128 -l authPriv -a SHA -A authkey1 -x AES -X privkey1 localhost .1.3.6

        auth_protocols = {'md5': config.usmHMACMD5AuthProtocol,
                          'sha': config.usmHMACSHAAuthProtocol,
                          'noauth': config.usmNoAuthProtocol}
        priv_protocols = {'des': config.usmDESPrivProtocol,
                          'aes': config.usmAesCfb128Protocol,
                          'nopriv': config.usmNoPrivProtocol}

        for auth in self.auth_config:
            user_name = auth.user_name
            auth_protocol = auth.auth_protocol if auth.auth_protocol else 'noauth'
            auth_protocol = auth_protocols.get(auth_protocol, None)
            auth_key = auth.auth_key
            priv_protocol = auth.priv_protocol if auth.priv_protocol else 'nopriv'
            priv_protocol = priv_protocols.get(priv_protocol, None)
            priv_key = auth.priv_key if auth.priv_key else None
            security_level = 'authPriv' if priv_protocol else 'authNoPriv'

            read_sub_tree = (1, 3, 6)

            engine.addV3User(user_name, auth_protocol, auth_key, priv_protocol, priv_key)
            engine.addVacmUser(3, user_name, security_level, read_sub_tree)

    def run(self):
        self.transport_dispatcher = AsyncoreDispatcher()
        self.transport_dispatcher.registerRoutingCbFun(lambda td, t, d: td)

        for idx, unity in enumerate(self.unity_config):
            transport_domain = udp.domainName + (idx,)
            engine = snmp_engine.SNMPEngine()
            engine.registerTransportDispatcher(self.transport_dispatcher, transport_domain)

            port = int(unity.port)
            engine.addTransport('0.0.0.0', port, idx)

            # self.add_users(engine)

            # Add v3 user
            # snmpget -v3 -u usr-md5-des -l authPriv -A authkey1 -X privkey1 192.168.56.1 1.3.6.1.4.1.1139.103.2.2.0
            user_name = 'usr-md5-des'
            security_level = 'authPriv'
            auth_key = 'authkey1'
            priv_key = 'privkey1'
            # read_sub_tree = (1, 3, 6, 1, 4, 1, 1139, 103, 2)
            read_sub_tree = (1, 3, 6)

            # engine.addV3User(user_name, config.usmHMACMD5AuthProtocol, auth_key,
            #                  config.usmDESPrivProtocol, priv_key)
            # engine.addVacmUser(3, user_name, security_level, read_sub_tree)

            # Add v1/v2c user
            # snmpget -v2c -c public 192.168.56.1 1.3.6.1.4.1.1139.103.2.1.0
            engine.addV1System(user_name, 'public')
            engine.addVacmUser(2, user_name, 'noAuthNoPriv', read_sub_tree, read_sub_tree)

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
    config_file = os.path.abspath('../etc/snmpagent.conf')
    agent = SNMPAgent(config_file)
    agent.parse_config()
    agent.run()
