import logging
import random
import time
import unittest

import snmpagent_unity
from snmpagent_unity.comptests import cli_helper
from snmpagent_unity.comptests import snmpclient
from snmpagent_unity.comptests import utils as comp_utils

LOG = logging.getLogger(__name__)


def get_scalar_mib(mib_name):
    return mib_name + '.0'


class SNMPv3User(object):
    def __init__(self, name, auth, auth_key, priv=None, priv_key=None):
        self.name = name
        self.auth = auth
        self.auth_key = auth_key
        self.priv = priv
        self.priv_key = priv_key


class TestSnmpUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.helper = cli_helper.Helper()
        cls.helper.stop_service()
        cls.helper.clear_access_data()

        config = comp_utils.get_env_yaml()
        cls.agent_ip = config.get('agent').get('ip')
        cls.agent_port = random.choice(config.get('agent').get('ports'))
        LOG.info('SNMP Agent port to be tested: {}'.format(cls.agent_port))

        # Add snmpv2 communities in agent
        cls.communities = []
        for v2_user in config.get('v2_user'):
            community = v2_user.get('name')
            cls.helper.create_community(community)
            cls.communities.append(community)

        # Add snmpv3 users in agent
        cls.users = {}
        for v3_user in config.get('v3_user'):
            name = v3_user.get('name')
            auth = v3_user.get('auth')
            auth_key = v3_user.get('auth_key')
            priv = v3_user.get('priv')
            priv_key = v3_user.get('priv_key')
            cls.helper.add_user(name, auth, auth_key, priv, priv_key)
            cls.users[name] = SNMPv3User(name, auth, auth_key, priv, priv_key)

        # User with md5 auth protocol for testing
        cls.user_md5_des = cls.users.get('user-md5-des')
        cls.user_md5_aes = cls.users.get('user-md5-aes')
        cls.user_md5 = cls.users.get('user-md5')
        # User with sha auth protocol for testing
        cls.user_sha_des = cls.users.get('user-sha-des')
        cls.user_sha_aes = cls.users.get('user-sha-aes')
        cls.user_sha = cls.users.get('user-sha')

        # Start agent
        cls.helper.start_service()

        # Wait 10 sec to make sure agent service ready
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.helper.stop_service()
        cls.helper.clear_access_data()

    def _service_check(self, snmp_client):
        mib_name = 'agentVersion'
        result, time_used = snmp_client.get(mib_name)

        self.assertEqual(snmpagent_unity.__version__,
                         result.get(get_scalar_mib(mib_name)))

    def test_snmp_v2_community(self):
        for community in self.communities:
            snmp_client = snmpclient.SNMPv2Client(self.agent_ip,
                                                  self.agent_port,
                                                  community)
            self._service_check(snmp_client)

    def test_v3_user_md5_des(self):
        snmp_client = snmpclient.SNMPv3Client(
            self.agent_ip, self.agent_port, self.user_md5_des.name,
            auth_key=self.user_md5_des.auth_key,
            priv_key=self.user_md5_des.priv_key)
        self._service_check(snmp_client)

    def test_v3_user_md5_aes(self):
        snmp_client = snmpclient.SNMPv3Client(
            self.agent_ip, self.agent_port, self.user_md5_aes.name,
            auth_key=self.user_md5_aes.auth_key,
            priv_key=self.user_md5_aes.priv_key,
            priv_proto=self.user_md5_aes.priv.lower())
        self._service_check(snmp_client)

    def test_v3_user_md5(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_md5.name,
                                              auth_key=self.user_md5.auth_key)
        self._service_check(snmp_client)

    def test_v3_user_sha_des(self):
        snmp_client = snmpclient.SNMPv3Client(
            self.agent_ip, self.agent_port, self.user_sha_des.name,
            auth_key=self.user_sha_des.auth_key,
            priv_key=self.user_sha_des.priv_key,
            auth_proto=self.user_sha_des.auth.lower(),
            priv_proto=self.user_sha_des.priv.lower())
        self._service_check(snmp_client)

    def test_v3_user_sha_aes(self):
        snmp_client = snmpclient.SNMPv3Client(
            self.agent_ip, self.agent_port, self.user_sha_aes.name,
            auth_key=self.user_sha_aes.auth_key,
            priv_key=self.user_sha_aes.priv_key,
            auth_proto=self.user_sha_aes.auth.lower(),
            priv_proto=self.user_sha_aes.priv.lower())
        self._service_check(snmp_client)

    def test_v3_user_sha(self):
        snmp_client = snmpclient.SNMPv3Client(
            self.agent_ip, self.agent_port, self.user_sha.name,
            auth_key=self.user_sha.auth_key,
            auth_proto=self.user_sha.auth.lower())
        self._service_check(snmp_client)

    def test_not_exists_user(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              'user-not-exists',
                                              auth_key='test1234')
        mib_name = 'agentVersion'
        result, time_used = snmp_client.get(mib_name)
        self.assertFalse(result)

    def test_wrong_auth_key(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_md5.name,
                                              auth_key='wront_auth_key')
        mib_name = 'agentVersion'
        result, time_used = snmp_client.get(mib_name)
        self.assertFalse(result)

    def test_wrong_priv_key(self):
        snmp_client = snmpclient.SNMPv3Client(self.agent_ip, self.agent_port,
                                              self.user_md5_aes.name,
                                              auth_key='test1234',
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
