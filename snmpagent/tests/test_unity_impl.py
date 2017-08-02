import unittest

import ddt
import mock
from snmpagent.unity_impl import AgentVersion, MibVersion


@ddt.ddt
class TestUnityClient(unittest.TestCase):
    def setUp(self):
        self.name = 'oid'
        self.idx = 0

    @mock.patch('snmpagent.clients.UnityClient')
    def test_agent_version(self, unity_client):
        unity_client.get_agent_version.return_value = '1.0'
        obj = AgentVersion.AgentVersion()
        self.assertEqual('1.0',
                         obj.read_get(self.name, self.idx, unity_client))

    @mock.patch('snmpagent.clients.UnityClient')
    def test_mib_version(self, unity_client):
        unity_client.get_mib_version.return_value = '1.0'
        obj = MibVersion.MibVersion()
        self.assertEqual('1.0',
                         obj.read_get(self.name, self.idx, unity_client))
