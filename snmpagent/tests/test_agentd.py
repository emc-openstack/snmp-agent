import unittest
import sys
import os

import mock

import snmpagent
from snmpagent import agentd
from snmpagent.tests import patches


class TestWindowsDaemon(unittest.TestCase):
    def setUp(self):
        # cleanup pid file due to test failure
        try:
            os.remove(agentd.WindowsDaemon.get_pid_file())
        except WindowsError:
            pass

        self.default_agent_conf = os.path.join(os.path.dirname(__file__),
                                               'test_data', 'configs',
                                               'agent.conf')

    @patches.psutil_process
    def test_already_exists(self, fake_process):
        pid_file = agentd.WindowsDaemon.get_pid_file()
        fake_process().cmdline = mock.Mock(
            return_value=['python', snmpagent.SERVICE_NAME])
        with open(pid_file, 'w') as f:
            f.write("1111")
        r = agentd.WindowsDaemon.exists()
        self.assertTrue(r)

    @patches.subprocess
    @patches.patch_get_access_path()
    def test_start(self, fake_popen):
        agentd.WindowsDaemon.start(self.default_agent_conf)
        self.assertEqual(sys.executable, fake_popen.args[0][0])
        self.assertEqual(self.default_agent_conf, fake_popen.args[0][2])

    @patches.psutil_process
    def test_stop(self, fake_process):
        pid_file = agentd.WindowsDaemon.get_pid_file()
        with open(pid_file, 'w') as f:
            f.write("1111")
        agentd.WindowsDaemon.stop()
        fake_process().terminate.assert_called_with()

    @patches.psutil_process
    def test_stop_already_stopped(self, fake_process):
        agentd.WindowsDaemon.stop()
        fake_process.terminate.assert_not_called()


class TestLinuxDaemon(unittest.TestCase):
    def setUp(self):
        # cleanup pid file due to test failure
        try:
            os.remove(agentd.LinuxDaemon.get_pid_file())
        except WindowsError:
            pass
        self.default_agent_conf = os.path.join(os.path.dirname(__file__),
                                               'test_data', 'configs',
                                               'agent.conf')

    @patches.subprocess
    @patches.patch_get_access_path()
    def test_start(self, fake_popen):
        agentd.LinuxDaemon.start(self.default_agent_conf)
        self.assertEqual(sys.executable, fake_popen.args[0][0])
        self.assertEqual(self.default_agent_conf, fake_popen.args[0][2])
