import unittest

import snmpagent_unity
from snmpagent_unity.comptests import snmpclient


def get_scalar_mib(mib_name):
    return mib_name + '.0'


class TestSnmpUser(unittest.TestCase):
    def setUp(self):
        self.agent_ip = '127.0.0.1'
        self.agent_port = 11161

        self.community = 'public'

        self.user_md5_des = 'user-md5-des'
        self.user_md5_aes = 'user-md5-aes'
        self.user_md5 = 'user-md5'

        self.user_sha_des = 'user-sha-des'
        self.user_sha_aes = 'user-sha-aes'
        self.user_sha = 'user-sha'

        self.auth_key = '12345678'
        self.priv_key = '12345678'

    def _service_check(self, snmp_client):
        mib_name = 'agentVersion'
        result, time_used = snmp_client.get(mib_name)

        self.assertEqual(snmpagent_unity.__version__,
                         result.get(get_scalar_mib(mib_name)))

    def test_snmp_v2_community(self):
        snmp_client = snmpclient.SNMPv2Client(self.agent_ip, self.agent_port,
                                              self.community)
        self._service_check(snmp_client)

    def test_v3_user_md5_des(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_md5_des,
                                              auth_key=self.auth_key,
                                              priv_key=self.priv_key)
        self._service_check(snmp_client)

    def test_v3_user_md5_aes(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_md5_aes,
                                              auth_key=self.auth_key,
                                              priv_key=self.priv_key,
                                              priv_proto='aes')
        self._service_check(snmp_client)

    def test_v3_user_md5(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_md5,
                                              auth_key=self.auth_key)
        self._service_check(snmp_client)

    def test_v3_user_sha_des(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_sha_des,
                                              auth_key=self.auth_key,
                                              priv_key=self.priv_key,
                                              auth_proto='sha',
                                              priv_proto='des')
        self._service_check(snmp_client)

    def test_v3_user_sha_aes(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_sha_aes,
                                              auth_key=self.auth_key,
                                              priv_key=self.priv_key,
                                              auth_proto='sha',
                                              priv_proto='aes')
        self._service_check(snmp_client)

    def test_v3_user_sha(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_sha,
                                              auth_key=self.auth_key,
                                              auth_proto='sha')
        self._service_check(snmp_client)

    def test_not_exists_user(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              'user-not-exists',
                                              auth_key=self.auth_key)
        mib_name = 'agentVersion'
        result, time_used = snmp_client.get(mib_name)
        self.assertFalse(result)

    def test_wrong_auth_key(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_md5,
                                              auth_key='wront_auth_key')
        mib_name = 'agentVersion'
        result, time_used = snmp_client.get(mib_name)
        self.assertFalse(result)

    def test_wrong_priv_key(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_md5_aes,
                                              auth_key=self.auth_key,
                                              priv_key='wrong_priv_key',
                                              priv_proto='aes')
        mib_name = 'agentVersion'
        result, time_used = snmp_client.get(mib_name)
        self.assertFalse(result)

    def test_wrong_community(self):
        snmp_client = snmpclient.SNMPv2Client(self.agent_ip, self.agent_port,
                                              'wrong_community')
        mib_name = 'agentVersion'
        result, time_used = snmp_client.get(mib_name)
        self.assertFalse(result)
