import collections
import unittest

from snmpagent import agent, enums
from snmpagent.tests import patches

SERVICE_ID_MD5 = (1, 3, 6, 1, 6, 3, 10, 1, 1, 2)
SERVICE_ID_SHA = (1, 3, 6, 1, 6, 3, 10, 1, 1, 3)
SERVICE_ID_DES = (1, 3, 6, 1, 6, 3, 10, 1, 2, 2)
SERVICE_ID_AES = (1, 3, 6, 1, 6, 3, 10, 1, 2, 4)


class TestEngine(unittest.TestCase):
    @patches.user_v3_entry
    @patches.user_v2_entry
    @patches.agent_config_entry
    def setUp(self, agent_config_entry, user_v2_entry, user_v3_entry):
        self.agent_config_entry = agent_config_entry
        self.user_v2_entry = user_v2_entry
        self.user_v3_entry = user_v3_entry

        self.agent_config_entry.agent_ip = '192.168.0.101'
        self.agent_config_entry.agent_port = '11161'
        self.agent_config_entry.mgmt_ip = '10.0.0.10'
        self.agent_config_entry.cache_interval = '60'
        self.agent_config_entry.user = 'admin'
        self.agent_config_entry.password = 'password'

        self.user_v2_entry.mode = enums.UserVersion.V2
        self.user_v2_entry.name = 'userv2'
        self.user_v2_entry.community = 'public'

        self.user_v3_entry.mode = enums.UserVersion.V3
        self.user_v3_entry.name = 'userv3'
        self.user_v3_entry.auth_protocol = enums.AuthProtocol.MD5
        self.user_v3_entry.auth_key.raw = 'authkey1'
        self.user_v3_entry.priv_protocol = enums.PrivProtocol.AES
        self.user_v3_entry.priv_key.raw = 'privkey1'

    @patches.mock_engine
    @patches.mock_client
    @patches.mock_udp
    @patches.add_transport
    @patches.add_vacm_user
    @patches.add_v3_user
    @patches.add_v1_system
    @patches.user_v3_entry
    def test_create_engine(self, user_v3_entry, add_v1_system, add_v3_user,
                           add_vacm_user, *args, **kwargs):
        array_config = self.agent_config_entry

        user_v2 = self.user_v2_entry
        user_v3 = self.user_v3_entry

        user_v3_no_priv = user_v3_entry
        user_v3_no_priv.mode = enums.UserVersion.V3
        user_v3_no_priv.name = 'userv3_no_priv'
        user_v3_no_priv.auth_protocol = enums.AuthProtocol.SHA
        user_v3_no_priv.auth_key.raw = 'authkey1_no_priv'
        user_v3_no_priv.priv_protocol = None
        user_v3_no_priv.priv_key.raw = None

        access_config = collections.OrderedDict()
        access_config[user_v2.name] = user_v2
        access_config[user_v3.name] = user_v3
        access_config[user_v3_no_priv.name] = user_v3_no_priv

        snmp_engine = agent.SNMPEngine(array_config, access_config)

        add_v1_system.assert_called_once()
        _, name, community = add_v1_system.call_args[0]
        self.assertEqual(name, user_v2.name)
        self.assertEqual(community, user_v2.community)

        self.assertEqual(add_v3_user.call_count, 2)

        _, name, auth_proto, auth_key, priv_proto, priv_key = \
            add_v3_user.call_args_list[0][0]
        self.assertEqual(name, user_v3.name)
        self.assertEqual(auth_proto, SERVICE_ID_MD5)
        self.assertEqual(auth_key, user_v3.auth_key.raw)
        self.assertEqual(priv_proto, SERVICE_ID_AES)
        self.assertEqual(priv_key, user_v3.priv_key.raw)

        _, name, auth_proto, auth_key = add_v3_user.call_args_list[1][0]
        self.assertEqual(name, user_v3_no_priv.name)
        self.assertEqual(auth_proto, SERVICE_ID_SHA)
        self.assertEqual(auth_key, user_v3_no_priv.auth_key.raw)

        self.assertEqual(add_vacm_user.call_count, 3)

        client_name = '{}_{}'.format(array_config.mgmt_ip,
                                     array_config.agent_port)
        kwargs['get_unity_client'].assert_called_once_with(
            client_name, array_config.mgmt_ip, array_config.user,
            array_config.password,
            cache_interval=int(array_config.cache_interval))

        self.assertEqual(snmp_engine.ip, array_config.agent_ip)
        self.assertEqual(snmp_engine.port, int(array_config.agent_port))
        self.assertEqual(snmp_engine.engine.parent, snmp_engine)
        self.assertNotEqual(snmp_engine.engine.unity_client, None)
        self.assertEqual(len(snmp_engine.engine.msgAndPduDsp.
                             mibInstrumController.mibBuilder.
                             mibSymbols['Unity-MIB']), 179)
        self.assertEqual(len(snmp_engine.engine.msgAndPduDsp.
                             mibInstrumController.mibBuilder.
                             mibSymbols['Exported-Unity-MIB']), 148)

    @patches.mock_engine
    @patches.mock_client
    @patches.mock_udp
    @patches.add_transport
    @patches.add_vacm_user
    @patches.add_v3_user
    @patches.add_v1_system
    @patches.agent_config_entry
    def test_create_engine_with_default_ip_port(self, agent_config_entry,
                                                *args, **kwargs):
        array_config = agent_config_entry

        array_config.agent_ip = None
        array_config.agent_port = None
        array_config.mgmt_ip = '10.0.0.10'
        array_config.cache_interval = '60'
        array_config.user = 'admin'
        array_config.password = 'password'

        user_v2 = self.user_v2_entry
        user_v3 = self.user_v3_entry

        access_config = collections.OrderedDict()
        access_config[user_v2.name] = user_v2
        access_config[user_v3.name] = user_v3

        snmp_engine = agent.SNMPEngine(array_config, access_config)

        client_name = '{}_{}'.format(array_config.mgmt_ip,
                                     array_config.agent_port)
        kwargs['get_unity_client'].assert_called_once_with(
            client_name, array_config.mgmt_ip, array_config.user,
            array_config.password,
            cache_interval=int(array_config.cache_interval))

        self.assertEqual(snmp_engine.ip, '0.0.0.0')
        self.assertEqual(snmp_engine.port, 161)
        self.assertEqual(snmp_engine.engine.parent, snmp_engine)
        self.assertNotEqual(snmp_engine.engine.unity_client, None)
        self.assertEqual(len(snmp_engine.engine.msgAndPduDsp.
                             mibInstrumController.mibBuilder.
                             mibSymbols['Unity-MIB']), 179)
        self.assertEqual(len(snmp_engine.engine.msgAndPduDsp.
                             mibInstrumController.mibBuilder.
                             mibSymbols['Exported-Unity-MIB']), 148)

    @patches.mock_engine
    @patches.mock_client
    @patches.mock_udp
    @patches.add_transport
    @patches.add_vacm_user
    @patches.add_v3_user
    @patches.add_v1_system
    def test_create_engine_with_invalid_user(self, add_v1_system,
                                             *args, **kwargs):
        array_config = self.agent_config_entry

        user_v2 = self.user_v2_entry
        user_v3 = self.user_v3_entry

        access_config = collections.OrderedDict()
        access_config[user_v2.name] = user_v2
        access_config[user_v3.name] = user_v3

        add_v1_system.side_effect = Exception('err')

        snmp_engine = agent.SNMPEngine(array_config, access_config)

        self.assertEqual(snmp_engine.ip, array_config.agent_ip)
        self.assertEqual(snmp_engine.port, int(array_config.agent_port))
        self.assertEqual(snmp_engine.engine.parent, snmp_engine)
        self.assertNotEqual(snmp_engine.engine.unity_client, None)
        self.assertEqual(len(snmp_engine.engine.msgAndPduDsp.
                             mibInstrumController.mibBuilder.
                             mibSymbols['Unity-MIB']), 179)
        self.assertEqual(len(snmp_engine.engine.msgAndPduDsp.
                             mibInstrumController.mibBuilder.
                             mibSymbols['Exported-Unity-MIB']), 148)

    @patches.mock_engine
    @patches.mock_client
    @patches.mock_udp
    @patches.add_transport
    @patches.add_vacm_user
    @patches.add_v3_user
    @patches.add_v1_system
    def test_create_engine_failed_to_connect_unity(self, *args, **kwargs):
        array_config = self.agent_config_entry

        user_v2 = self.user_v2_entry
        user_v3 = self.user_v3_entry

        access_config = collections.OrderedDict()
        access_config[user_v2.name] = user_v2
        access_config[user_v3.name] = user_v3

        kwargs['get_unity_client'].side_effect = Exception('err')

        snmp_engine = agent.SNMPEngine(array_config, access_config)

        self.assertEqual(snmp_engine.ip, array_config.agent_ip)
        self.assertEqual(snmp_engine.port, int(array_config.agent_port))
        self.assertEqual(snmp_engine.engine.parent, snmp_engine)
        self.assertEqual(snmp_engine.engine.unity_client, None)
        self.assertEqual(len(snmp_engine.engine.msgAndPduDsp.
                             mibInstrumController.mibBuilder.
                             mibSymbols['Unity-MIB']), 179)
        self.assertEqual(len(snmp_engine.engine.msgAndPduDsp.
                             mibInstrumController.mibBuilder.
                             mibSymbols['Exported-Unity-MIB']), 148)
