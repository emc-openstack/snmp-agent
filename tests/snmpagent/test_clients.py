# import mock
import sys
import unittest

from storops import UnitySystem
import storops
from unittest.mock import patch, Mock, MagicMock


# from ddt import ddt, data, file_data, unpack

sys.path.append('..\\..\\')
# from snmpagent.clients import UnityClient
import snmpagent.clients


# class UnityClient(object):
#     def __init__(self):
#         self.client = UnitySystem()
#
#     def get_xx(self):
#         print(self.client.get_sp())


class MockUnitySystem(object):
    def __init__(self):
        self.model = 'model 100'

    def enable_perf_stats(self):
        pass

    def get_sp(self):
        return 100

    # def __getattr__(self, item):
    #     import pdb; pdb.set_trace()

    def get_sps(self):
        return [1, 2, 3]


# @ddt
class TestUnityClient(unittest.TestCase):
    @patch(target='storops.UnitySystem')
    def setUp(self, mock_unity_system):
        print('setting up')
        # mock_unity_system.return_value = Mock()
        mock_unity_system.return_value = MockUnitySystem()
        self.uc = snmpagent.clients.UnityClient()

    def tearDown(self):
        print('tearing down')

    def test_get_sp(self):
        print(self.uc.get_sp())
        self.assertEqual(self.uc.get_sp(), 10)

    def test_get_sp2(self):
        print(self.uc.get_sp())

    def test_get_model(self):
        print(self.uc.get_model())

    # @patch(target='storops.UnitySystem')
    # def test_get_serial_number(self, mock_unity_system):
    #     mock_unity_system.return_value = MagicMock()
    #     # mock_unity_system.serial_number = MagicMock(return_value='abc')
    #     self.uc = snmpagent.clients.UnityClient()
    #     print(self.uc.get_serial_number())

class TestUnityImpl(unittest.TestCase):
    @patch()
    def test_agent_version(self):
        pass