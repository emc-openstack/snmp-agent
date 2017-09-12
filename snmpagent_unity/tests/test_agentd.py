import unittest
import sys
import os

import mock

from snmpagent_unity import agentd
from snmpagent_unity.tests import patches


def cleanup_pid(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


class TestWindowsDaemon(unittest.TestCase):
    def setUp(self):
        self.default_agent_conf = os.path.join(os.path.dirname(__file__),
                                               'test_data', 'configs',
                                               'agent.conf')

    @patches.psutil_process
    @patches.patch_get_pid_file
    def test_already_exists(self, fake_process):
        pid_file = agentd.WindowsDaemon.get_pid_file()
        self.addCleanup(cleanup_pid, pid_file)
        fake_process().cmdline = mock.Mock(
            return_value=['python', 'snmpagent_unity/agentd.py'])
        with open(pid_file, 'w') as f:
            f.write("1111")
        r = agentd.WindowsDaemon.exists()
        self.assertIsNotNone(r)

    @patches.subprocess
    @patches.patch_get_access_path()
    @patches.patch_get_pid_file
    def test_start(self, fake_popen):
        pid_file = agentd.WindowsDaemon.get_pid_file()
        self.addCleanup(cleanup_pid, pid_file)
        agentd.WindowsDaemon.start(self.default_agent_conf)
        self.assertEqual(sys.executable, fake_popen.args[0][0])
        self.assertEqual(self.default_agent_conf, fake_popen.args[0][2])

    @patches.psutil_process
    @patches.patch_get_pid_file
    def test_stop(self, fake_process):
        pid_file = agentd.WindowsDaemon.get_pid_file()
        self.addCleanup(cleanup_pid, pid_file)

        with open(pid_file, 'w') as f:
            f.write("1111")
        fake_process().cmdline = mock.Mock(
            return_value=['python', 'snmpagent_unity/agentd.py'])
        r = agentd.WindowsDaemon.stop()
        self.assertEqual(0, r)
        fake_process().terminate.assert_called_with()

    @patches.psutil_process
    @patches.patch_get_pid_file
    def test_stop_already_stopped(self, fake_process):
        r = agentd.WindowsDaemon.stop()
        self.assertEqual(2, r)
        fake_process.terminate.assert_not_called()


class TestLinuxDaemon(unittest.TestCase):
    def setUp(self):
        self.default_agent_conf = os.path.join(os.path.dirname(__file__),
                                               'test_data', 'configs',
                                               'agent.conf')

    @patches.subprocess
    @patches.patch_get_access_path()
    @patches.patch_get_pid_file
    def test_start(self, fake_popen):
        pid_file = agentd.WindowsDaemon.get_pid_file()
        self.addCleanup(cleanup_pid, pid_file)

        agentd.LinuxDaemon.start(self.default_agent_conf)
        self.assertEqual(sys.executable, fake_popen.args[0][0])
        self.assertEqual(self.default_agent_conf, fake_popen.args[0][2])
