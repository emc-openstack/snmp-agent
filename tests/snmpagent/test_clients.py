import os
import pytest

from .unityclient_mock import MockUnityClient


@pytest.fixture()
def unity_client(request):
    return MockUnityClient(request.param)


# class TestSystem(object):
#     path = '.\\unity_data\\disk\\all.json'
#
#     @pytest.fixture(scope='class')
#     def client(self, unity_client):
#         return unity_client()
#
#     # @pytest.fixture(autouse=True)
#     def test_get_agent_version(self, unity_client):
#         # pytest.set_trace()
#         assert unity_client.get_agent_version() == '1.0'
#
#     def test_get_mib_version(self, unity_client):
#         assert unity_client.get_mib_version() == '1.0'


# @pytest.mark.usefixtures('unity_client')
# @pytest.mark.parametrize('unity_client', ['.\\unity_data\\disk\\all.json',], indirect=True)
# class TestDisk(object):
#     name = 'DAE 0 1 Disk 0'
#
#     # def test_get_disks(self):
#     #     pass
#
#     def test_get_disk_model(self, unity_client):
#         assert unity_client.get_disk_model(name=self.name) == 'ST2000NK EMC2000'



dir_battery = os.path.abspath('./unity_data/battery/')
path_battery_positive = os.path.join(dir_battery, "battery_positive.json")
@pytest.mark.parametrize('unity_client', [path_battery_positive], indirect=True)
class TestBattery(object):
    name = 'SP A Battery 0'

    def test_get_bbus(self, unity_client):
        actual = unity_client.get_bbus()
        expected = ['SP A Battery 0', 'SP B Battery 0']
        assert len(actual) == len(expected)
        assert set(actual) == set(expected)

    def test_get_bbu_manufacturer(self, unity_client):
        assert unity_client.get_bbu_manufacturer(name=self.name) == 'ACBEL POLYTECH INC.'

    def test_get_bbu_model(self, unity_client):
        assert unity_client.get_bbu_model(name=self.name) == 'LITHIUM-ION, UNIVERSAL BOB'

    def test_get_bbu_firmware_version(self, unity_client):
        assert unity_client.get_bbu_firmware_version(name=self.name) == '073.91'
    def test_get_bbu_parent_sp(self, unity_client):
        assert unity_client.get_bbu_parent_sp(name=self.name) == 'SP A'

    def test_get_bbu_health_status(self, unity_client):
        assert unity_client.get_bbu_health_status(name=self.name) == 'OK'
