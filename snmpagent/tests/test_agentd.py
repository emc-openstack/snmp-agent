import unittest
import sys
import os

from snmpagent import agentd
from snmpagent.tests import patches


class TestWindowsDaemon(unittest.TestCase):
    def setUp(self):
        # cleanup pid file due to test failure
        try:
            os.remove(agentd.WindowsDaemon.get_pid_file())
        except WindowsError:
            pass

    @patches.subprocess
    def test_start(self, fake_popen):
        agentd.WindowsDaemon.start("fake.conf")
        self.assertEqual(sys.executable, fake_popen.args[0][0])
        self.assertEqual('fake.conf', fake_popen.args[0][2])

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

    @patches.subprocess
    def test_start(self, fake_popen):
        agentd.LinuxDaemon.start("fake.conf")
        self.assertEqual(sys.executable, fake_popen.args[0][0])
        self.assertEqual('fake.conf', fake_popen.args[0][2])
