import unittest

import ddt
from snmpagent import unity_impl
from snmpagent.tests import patches


@ddt.ddt
class TestUnityClient(unittest.TestCase):
    def setUp(self):
        self.name = 'oid'
        self.idx = 0
        self.test_string = 'test string'
        self.test_number = 100
        self.test_list = ['a', 'b', 'c']

    # system
    @patches.unity_client
    def test_agent_version(self, unity_client):
        unity_client.get_agent_version.return_value = self.test_string
        obj = unity_impl.AgentVersion.AgentVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_agent_version.assert_called_once()

    @patches.unity_client
    def test_mib_version(self, unity_client):
        unity_client.get_mib_version.return_value = self.test_string
        obj = unity_impl.MibVersion.MibVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_mib_version.assert_called_once()

    @patches.unity_client
    def test_manufacturer(self, unity_client):
        unity_client.get_manufacturer.return_value = self.test_string
        obj = unity_impl.Manufacturer.Manufacturer()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_manufacturer.assert_called_once()

    @patches.unity_client
    def test_model(self, unity_client):
        unity_client.get_model.return_value = self.test_string
        obj = unity_impl.Model.Model()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_model.assert_called_once()

    @patches.unity_client
    def test_serial_number(self, unity_client):
        unity_client.get_serial_number.return_value = self.test_string
        obj = unity_impl.SerialNumber.SerialNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_serial_number.assert_called_once()

    @patches.unity_client
    def test_operation_environment_version(self, unity_client):
        unity_client.get_operation_environment_version.return_value = self.test_string
        obj = unity_impl.OperationEnvironmentVersion.OperationEnvironmentVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_operation_environment_version.assert_called_once()

    @patches.unity_client
    def test_mgmt_ip(self, unity_client):
        unity_client.get_mgmt_ip.return_value = self.test_string
        obj = unity_impl.ManagementIP.ManagementIP()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_mgmt_ip.assert_called_once()

    @patches.unity_client
    def test_current_power(self, unity_client):
        unity_client.get_current_power.return_value = self.test_string
        obj = unity_impl.CurrentPower.CurrentPower()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_current_power.assert_called_once()

    @patches.unity_client
    def test_avg_power(self, unity_client):
        unity_client.get_avg_power.return_value = self.test_string
        obj = unity_impl.AveragePower.AveragePower()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_avg_power.assert_called_once()

    @patches.unity_client
    def test_number_of_sp(self, unity_client):
        unity_client.get_number_of_sp.return_value = self.test_number
        obj = unity_impl.NumberOfStorageProcessor.NumberOfStorageProcessor()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_sp.assert_called_once()

    @patches.unity_client
    def test_number_of_enclosure(self, unity_client):
        unity_client.get_number_of_enclosure.return_value = self.test_number
        obj = unity_impl.NumberOfEnclosure.NumberOfEnclosure()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_enclosure.assert_called_once()

    @patches.unity_client
    def test_number_of_power_supply(self, unity_client):
        unity_client.get_number_of_power_supply.return_value = self.test_number
        obj = unity_impl.NumberOfPowerSupply.NumberOfPowerSupply()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_power_supply.assert_called_once()

    @patches.unity_client
    def test_number_of_fan(self, unity_client):
        unity_client.get_number_of_fan.return_value = self.test_number
        obj = unity_impl.NumberOfFan.NumberOfFan()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_fan.assert_called_once()

    @patches.unity_client
    def test_number_of_disk(self, unity_client):
        unity_client.get_number_of_disk.return_value = self.test_number
        obj = unity_impl.NumberOfPhysicalDisk.NumberOfPhysicalDisk()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_disk.assert_called_once()

    @patches.unity_client
    def test_number_of_frontend_port(self, unity_client):
        unity_client.get_number_of_frontend_port.return_value = self.test_number
        obj = unity_impl.NumberOfFrontendPort.NumberOfFrontendPort()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_frontend_port.assert_called_once()

    @patches.unity_client
    def test_number_of_backend_port(self, unity_client):
        unity_client.get_number_of_backend_port.return_value = self.test_number
        obj = unity_impl.NumberOfBackendPort.NumberOfBackendPort()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_backend_port.assert_called_once()

    @patches.unity_client
    def test_total_capacity(self, unity_client):
        unity_client.get_total_capacity.return_value = self.test_string
        obj = unity_impl.TotalCapacity.TotalCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_total_capacity.assert_called_once()

    @patches.unity_client
    def test_used_capacity(self, unity_client):
        unity_client.get_used_capacity.return_value = self.test_string
        obj = unity_impl.UsedCapacity.UsedCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_used_capacity.assert_called_once()

    @patches.unity_client
    def test_free_capacity(self, unity_client):
        unity_client.get_free_capacity.return_value = self.test_string
        obj = unity_impl.FreeCapacity.FreeCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_free_capacity.assert_called_once()

    @patches.unity_client
    def test_total_iops(self, unity_client):
        unity_client.get_total_iops.return_value = self.test_string
        obj = unity_impl.TotalThroughput.TotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_total_iops.assert_called_once()

    @patches.unity_client
    def test_read_iops(self, unity_client):
        unity_client.get_read_iops.return_value = self.test_string
        obj = unity_impl.ReadThroughput.ReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_read_iops.assert_called_once()

    @patches.unity_client
    def test_write_iops(self, unity_client):
        unity_client.get_write_iops.return_value = self.test_string
        obj = unity_impl.WriteThroughput.WriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_write_iops.assert_called_once()

    @patches.unity_client
    def test_total_byte_rate(self, unity_client):
        unity_client.get_total_byte_rate.return_value = self.test_string
        obj = unity_impl.TotalBandwidth.TotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_total_byte_rate.assert_called_once()

    @patches.unity_client
    def test_read_byte_rate(self, unity_client):
        unity_client.get_read_byte_rate.return_value = self.test_string
        obj = unity_impl.ReadBandwidth.ReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_read_byte_rate.assert_called_once()

    @patches.unity_client
    def test_write_byte_rate(self, unity_client):
        unity_client.get_write_byte_rate.return_value = self.test_string
        obj = unity_impl.WriteBandwidth.WriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_write_byte_rate.assert_called_once()

    # storageProcessorTable
    @patches.unity_client
    def test_sp_name(self, unity_client):
        obj = unity_impl.StorageProcessorName.StorageProcessorName()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_sp_name_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorName.StorageProcessorNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_serial_number(self, unity_client):
        unity_client.get_sp_serial_number.return_value = self.test_string
        obj = unity_impl.StorageProcessorSerialNumber.StorageProcessorSerialNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_serial_number.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_serial_number_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorSerialNumber.StorageProcessorSerialNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_op_state(self, unity_client):
        unity_client.get_sp_health_status.return_value = self.test_string
        obj = unity_impl.StorageProcessorOperationalState.StorageProcessorOperationalState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_op_state_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorOperationalState.StorageProcessorOperationalStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cpu_utilization(self, unity_client):
        unity_client.get_sp_utilization.return_value = self.test_string
        obj = unity_impl.StorageProcessorCpuUtilization.StorageProcessorCpuUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_utilization.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_cpu_utilization_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorCpuUtilization.StorageProcessorCpuUtilizationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_total_iops(self, unity_client):
        unity_client.get_sp_block_total_iops.return_value = self.test_string
        obj = unity_impl.StorageProcessorTotalThroughput.StorageProcessorTotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_total_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_total_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorTotalThroughput.StorageProcessorTotalThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_read_iops(self, unity_client):
        unity_client.get_sp_block_read_iops.return_value = self.test_string
        obj = unity_impl.StorageProcessorReadThroughput.StorageProcessorReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_read_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_read_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorReadThroughput.StorageProcessorReadThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_write_iops(self, unity_client):
        unity_client.get_sp_block_write_iops.return_value = self.test_string
        obj = unity_impl.StorageProcessorWriteThroughput.StorageProcessorWriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_write_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_write_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorWriteThroughput.StorageProcessorWriteThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_total_byte_rate(self, unity_client):
        unity_client.get_sp_total_byte_rate.return_value = self.test_string
        obj = unity_impl.StorageProcessorTotalBandwidth.StorageProcessorTotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_total_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_total_byte_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorTotalBandwidth.StorageProcessorTotalBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_read_byte_rate(self, unity_client):
        unity_client.get_sp_read_byte_rate.return_value = self.test_string
        obj = unity_impl.StorageProcessorReadBandwidth.StorageProcessorReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_read_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_read_byte_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorReadBandwidth.StorageProcessorReadBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_write_byte_rate(self, unity_client):
        unity_client.get_sp_write_byte_rate.return_value = self.test_string
        obj = unity_impl.StorageProcessorWriteBandwidth.StorageProcessorWriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_write_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_write_byte_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorWriteBandwidth.StorageProcessorWriteBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cache_dirty_size(self, unity_client):
        unity_client.get_sp_cache_dirty_size.return_value = self.test_string
        obj = unity_impl.StorageProcessorCacheDirtySize.StorageProcessorCacheDirtySize()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_cache_dirty_size.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_cache_dirty_size_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorCacheDirtySize.StorageProcessorCacheDirtySizeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cache_read_hit_ratio(self, unity_client):
        unity_client.get_sp_block_cache_read_hit_ratio.return_value = self.test_string
        obj = unity_impl.StorageProcessorReadCacheState.StorageProcessorReadCacheState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_cache_read_hit_ratio.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_sp_cache_read_hit_ratio_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorReadCacheState.StorageProcessorReadCacheStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cache_write_hit_ratio(self, unity_client):
        unity_client.get_sp_block_cache_write_hit_ratio.return_value = self.test_string
        obj = unity_impl.StorageProcessorWriteCacheState.StorageProcessorWriteCacheState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_cache_write_hit_ratio.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_sp_cache_write_hit_ratio_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = unity_impl.StorageProcessorWriteCacheState.StorageProcessorWriteCacheStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    # poolTable
    @patches.unity_client
    def test_pool_name(self, unity_client):
        obj = unity_impl.PoolName.PoolName()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_pool_name_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = unity_impl.PoolName.PoolNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_disk_types(self, unity_client):
        unity_client.get_pool_disk_types.return_value = self.test_string
        obj = unity_impl.PoolDiskTypes.PoolDiskTypes()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_disk_types.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_disk_types_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = unity_impl.PoolDiskTypes.PoolDiskTypesColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_raid_levels(self, unity_client):
        unity_client.get_pool_raid_levels.return_value = self.test_string
        obj = unity_impl.PoolRaidLevels.PoolRaidLevels()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_raid_levels.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_raid_levels_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = unity_impl.PoolRaidLevels.PoolRaidLevelsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_fast_cache_status(self, unity_client):
        unity_client.get_pool_fast_cache_status.return_value = self.test_string
        obj = unity_impl.PoolFastCacheStatus.PoolFastCacheStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_fast_cache_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_pool_fast_cache_status_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = unity_impl.PoolFastCacheStatus.PoolFastCacheStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_number_of_disk(self, unity_client):
        unity_client.get_pool_number_of_disk.return_value = self.test_number
        obj = unity_impl.PoolNumberOfPhysicalDisk.PoolNumberOfPhysicalDisk()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_number_of_disk.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_number_of_disk_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = unity_impl.PoolNumberOfPhysicalDisk.PoolNumberOfPhysicalDiskColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_size_total(self, unity_client):
        unity_client.get_pool_size_total.return_value = self.test_string
        obj = unity_impl.PoolTotalCapacity.PoolTotalCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_size_total.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_size_total_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = unity_impl.PoolTotalCapacity.PoolTotalCapacityColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_size_free(self, unity_client):
        unity_client.get_pool_size_free.return_value = self.test_string
        obj = unity_impl.PoolRemainingCapacity.PoolRemainingCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_size_free.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_size_free_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = unity_impl.PoolRemainingCapacity.PoolRemainingCapacityColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_size_used(self, unity_client):
        unity_client.get_pool_size_used.return_value = self.test_string
        obj = unity_impl.PoolUsedCapacity.PoolUsedCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_size_used.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_size_used_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = unity_impl.PoolUsedCapacity.PoolUsedCapacityColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_size_ultilization(self, unity_client):
        unity_client.get_pool_size_ultilization.return_value = self.test_string
        obj = unity_impl.PoolCapacityUtilization.PoolCapacityUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_size_ultilization.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_pool_size_ultilization_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = unity_impl.PoolCapacityUtilization.PoolCapacityUtilizationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    # volumeTable
    @patches.unity_client
    def test_lun_id(self, unity_client):
        obj = unity_impl.VolumeId.VolumeId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_lun_id_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeId.VolumeIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_name(self, unity_client):
        unity_client.get_lun_name.return_value = self.test_string
        obj = unity_impl.VolumeName.VolumeName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_name_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeName.VolumeNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_raid_type(self, unity_client):
        unity_client.get_lun_raid_type.return_value = self.test_string
        obj = unity_impl.VolumeRaidLevels.VolumeRaidLevels()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_raid_type.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_raid_type_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeRaidLevels.VolumeRaidLevelsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_size_allocated(self, unity_client):
        unity_client.get_lun_size_allocated.return_value = self.test_string
        obj = unity_impl.VolumeAllocatedSize.VolumeAllocatedSize()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_size_allocated.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_size_allocated_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeAllocatedSize.VolumeAllocatedSizeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_size_total(self, unity_client):
        unity_client.get_lun_size_total.return_value = self.test_string
        obj = unity_impl.VolumeSize.VolumeSize()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_size_total.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_size_total_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeSize.VolumeSizeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_health_status(self, unity_client):
        unity_client.get_lun_health_status.return_value = self.test_string
        obj = unity_impl.VolumeOperationalState.VolumeOperationalState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_health_status_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeOperationalState.VolumeOperationalStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_fast_cache_status(self, unity_client):
        unity_client.get_lun_fast_cache_status.return_value = self.test_string
        obj = unity_impl.VolumeFastCacheState.VolumeFastCacheState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_fast_cache_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_lun_fast_cache_status_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeFastCacheState.VolumeFastCacheStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_default_sp(self, unity_client):
        unity_client.get_lun_default_sp.return_value = self.test_string
        obj = unity_impl.VolumeDefaultStorageProcessor.VolumeDefaultStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_default_sp.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_default_sp_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeDefaultStorageProcessor.VolumeDefaultStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_current_sp(self, unity_client):
        unity_client.get_lun_current_sp.return_value = self.test_string
        obj = unity_impl.VolumeCurrentStorageProcessor.VolumeCurrentStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_current_sp.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_current_sp_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeCurrentStorageProcessor.VolumeCurrentStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_response_time(self, unity_client):
        unity_client.get_lun_response_time.return_value = self.test_string
        obj = unity_impl.VolumeResponseTime.VolumeResponseTime()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_response_time.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_response_time_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeResponseTime.VolumeResponseTimeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_queue_length(self, unity_client):
        unity_client.get_lun_queue_length.return_value = self.test_string
        obj = unity_impl.VolumeQueueLength.VolumeQueueLength()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_queue_length.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_queue_length_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeQueueLength.VolumeQueueLengthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_total_iops(self, unity_client):
        unity_client.get_lun_total_iops.return_value = self.test_string
        obj = unity_impl.VolumeTotalThroughput.VolumeTotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_total_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_total_iops_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeTotalThroughput.VolumeTotalThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_read_iops(self, unity_client):
        unity_client.get_lun_read_iops.return_value = self.test_string
        obj = unity_impl.VolumeReadThroughput.VolumeReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_read_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_read_iops_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeReadThroughput.VolumeReadThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_write_iops(self, unity_client):
        unity_client.get_lun_write_iops.return_value = self.test_string
        obj = unity_impl.VolumeWriteThroughput.VolumeWriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_write_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_write_iops_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeWriteThroughput.VolumeWriteThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_fast_cache_read_hit_iops(self, unity_client):
        unity_client.get_lun_fast_cache_read_hits.return_value = self.test_string
        obj = unity_impl.VolumeFastCacheReadHitIOs.VolumeFastCacheReadHitIOs()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_fast_cache_read_hits.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_lun_fast_cache_read_hit_iops_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeFastCacheReadHitIOs.VolumeFastCacheReadHitIOsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_fast_cache_write_hit_iops(self, unity_client):
        unity_client.get_lun_fast_cache_write_hits.return_value = self.test_string
        obj = unity_impl.VolumeFastCacheWriteHitIOs.VolumeFastCacheWriteHitIOs()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_fast_cache_write_hits.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_lun_fast_cache_write_hit_iops_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeFastCacheWriteHitIOs.VolumeFastCacheWriteHitIOsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_total_byte_rate(self, unity_client):
        unity_client.get_lun_total_byte_rate.return_value = self.test_string
        obj = unity_impl.VolumeTotalBandwidth.VolumeTotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_total_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_total_byte_rate_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeTotalBandwidth.VolumeTotalBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_read_byte_rate(self, unity_client):
        unity_client.get_lun_read_byte_rate.return_value = self.test_string
        obj = unity_impl.VolumeReadBandwidth.VolumeReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_read_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_read_byte_rate_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeReadBandwidth.VolumeReadBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_write_byte_rate(self, unity_client):
        unity_client.get_lun_write_byte_rate.return_value = self.test_string
        obj = unity_impl.VolumeWriteBandwidth.VolumeWriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_write_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_write_byte_rate_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeWriteBandwidth.VolumeWriteBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_fast_cache_read_hit_rate(self, unity_client):
        unity_client.get_lun_fast_cache_read_hit_rate.return_value = self.test_string
        obj = unity_impl.VolumeFastCacheReadHitRate.VolumeFastCacheReadHitRate()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_fast_cache_read_hit_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_lun_fast_cache_read_hit_rate_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeFastCacheReadHitRate.VolumeFastCacheReadHitRateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_fast_cache_write_hit_rate(self, unity_client):
        unity_client.get_lun_fast_cache_write_hit_rate.return_value = self.test_string
        obj = unity_impl.VolumeFastCacheWriteHitRate.VolumeFastCacheWriteHitRate()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_fast_cache_write_hit_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_lun_fast_cache_write_hit_rate_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeFastCacheWriteHitRate.VolumeFastCacheWriteHitRateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_utilization(self, unity_client):
        unity_client.get_lun_utilization.return_value = self.test_string
        obj = unity_impl.VolumeUtilization.VolumeUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_utilization.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_utilization_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeUtilization.VolumeUtilizationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_host_access(self, unity_client):
        unity_client.get_lun_host_access.return_value = self.test_string
        obj = unity_impl.VolumeHostInfo.VolumeHostInfo()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_host_access.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_host_access_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = unity_impl.VolumeHostInfo.VolumeHostInfoColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    # diskTable
    @patches.unity_client
    def test_disk_name(self, unity_client):
        obj = unity_impl.DiskName.DiskName()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_disk_name_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskName.DiskNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_model(self, unity_client):
        unity_client.get_disk_model.return_value = self.test_string
        obj = unity_impl.DiskModel.DiskModel()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_model.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_model_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskModel.DiskModelColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_serial_number(self, unity_client):
        unity_client.get_disk_serial_number.return_value = self.test_string
        obj = unity_impl.DiskSerialNumber.DiskSerialNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_serial_number.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_serial_number_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskSerialNumber.DiskSerialNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_version(self, unity_client):
        unity_client.get_disk_version.return_value = self.test_string
        obj = unity_impl.DiskFirmwareVersion.DiskFirmwareVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_version.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_version_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskFirmwareVersion.DiskFirmwareVersionColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_type(self, unity_client):
        unity_client.get_disk_type.return_value = self.test_string
        obj = unity_impl.DiskType.DiskType()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_type.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_type_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskType.DiskTypeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_slot_number(self, unity_client):
        unity_client.get_disk_slot_number.return_value = self.test_string
        obj = unity_impl.DiskPhysicalLocation.DiskPhysicalLocation()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_slot_number.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_slot_number_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskPhysicalLocation.DiskPhysicalLocationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_status(self, unity_client):
        unity_client.get_disk_health_status.return_value = self.test_string
        obj = unity_impl.DiskStatus.DiskStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_status_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskStatus.DiskStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_raw_size(self, unity_client):
        unity_client.get_disk_raw_size.return_value = self.test_string
        obj = unity_impl.DiskRawCapacity.DiskRawCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_raw_size.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_raw_size_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskRawCapacity.DiskRawCapacityColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_current_pool(self, unity_client):
        unity_client.get_disk_current_pool.return_value = self.test_string
        obj = unity_impl.DiskCurrentPool.DiskCurrentPool()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_current_pool.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_current_pool_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskCurrentPool.DiskCurrentPoolColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_response_time(self, unity_client):
        unity_client.get_disk_response_time.return_value = self.test_string
        obj = unity_impl.DiskResponseTime.DiskResponseTime()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_response_time.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_response_time_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskResponseTime.DiskResponseTimeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_queue_length(self, unity_client):
        unity_client.get_disk_queue_length.return_value = self.test_string
        obj = unity_impl.DiskQueueLength.DiskQueueLength()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_queue_length.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_queue_length_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskQueueLength.DiskQueueLengthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_total_iops(self, unity_client):
        unity_client.get_disk_total_iops.return_value = self.test_string
        obj = unity_impl.DiskTotalThroughput.DiskTotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_total_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_total_iops_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskTotalThroughput.DiskTotalThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_read_iops(self, unity_client):
        unity_client.get_disk_read_iops.return_value = self.test_string
        obj = unity_impl.DiskReadThroughput.DiskReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_read_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_read_iops_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskReadThroughput.DiskReadThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_write_iops(self, unity_client):
        unity_client.get_disk_write_iops.return_value = self.test_string
        obj = unity_impl.DiskWriteThroughput.DiskWriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_write_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_write_iops_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskWriteThroughput.DiskWriteThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_total_byte_rate(self, unity_client):
        unity_client.get_disk_total_byte_rate.return_value = self.test_string
        obj = unity_impl.DiskTotalBandwidth.DiskTotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_total_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_total_byte_rate_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskTotalBandwidth.DiskTotalBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_read_byte_rate(self, unity_client):
        unity_client.get_disk_read_byte_rate.return_value = self.test_string
        obj = unity_impl.DiskReadBandwidth.DiskReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_read_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_read_byte_rate_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskReadBandwidth.DiskReadBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_write_byte_rate(self, unity_client):
        unity_client.get_disk_write_byte_rate.return_value = self.test_string
        obj = unity_impl.DiskWriteBandwidth.DiskWriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_write_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_write_byte_rate_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskWriteBandwidth.DiskWriteBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_utilization(self, unity_client):
        unity_client.get_disk_utilization.return_value = self.test_string
        obj = unity_impl.DiskUtilization.DiskUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_utilization.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_utilization_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = unity_impl.DiskUtilization.DiskUtilizationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    # frontendPortTable
    @patches.unity_client
    def test_frontend_port_id(self, unity_client):
        unity_client.get_frontend_port_id.return_value = self.test_string
        obj = unity_impl.FrontendPortId.FrontendPortId()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_id.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_frontend_port_id_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortId.FrontendPortIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_name(self, unity_client):
        unity_client.get_frontend_port_name.return_value = self.test_string
        obj = unity_impl.FrontendPortName.FrontendPortName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_frontend_port_name_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortName.FrontendPortNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_address(self, unity_client):
        unity_client.get_frontend_port_address.return_value = self.test_string
        obj = unity_impl.FrontendPortAddress.FrontendPortAddress()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_address.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_address_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortAddress.FrontendPortAddressColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_type(self, unity_client):
        unity_client.get_frontend_port_type.return_value = self.test_string
        obj = unity_impl.FrontendPortType.FrontendPortType()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_type.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_frontend_port_type_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortType.FrontendPortTypeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_current_speed(self, unity_client):
        unity_client.get_frontend_port_current_speed.return_value = self.test_string
        obj = unity_impl.FrontendPortCurrentSpeed.FrontendPortCurrentSpeed()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_current_speed.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_current_speed_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortCurrentSpeed.FrontendPortCurrentSpeedColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_support_speed(self, unity_client):
        unity_client.get_frontend_port_supported_speed.return_value = self.test_string
        obj = unity_impl.FrontendPortSupportedSpeed.FrontendPortSupportedSpeed()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_supported_speed.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_support_speed_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortSupportedSpeed.FrontendPortSupportedSpeedColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_status(self, unity_client):
        unity_client.get_frontend_port_health_status.return_value = self.test_string
        obj = unity_impl.FrontendPortStatus.FrontendPortStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_health_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_status_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortStatus.FrontendPortStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_total_iops(self, unity_client):
        unity_client.get_frontend_port_total_iops.return_value = self.test_string
        obj = unity_impl.FrontendPortTotalThroughput.FrontendPortTotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_total_iops.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_total_iops_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortTotalThroughput.FrontendPortTotalThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_read_iops(self, unity_client):
        unity_client.get_frontend_port_read_iops.return_value = self.test_string
        obj = unity_impl.FrontendPortReadThroughput.FrontendPortReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_read_iops.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_read_iops_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortReadThroughput.FrontendPortReadThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_write_iops(self, unity_client):
        unity_client.get_frontend_port_write_iops.return_value = self.test_string
        obj = unity_impl.FrontendPortWriteThroughput.FrontendPortWriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_write_iops.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_write_iops_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortWriteThroughput.FrontendPortWriteThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_total_byte_rate(self, unity_client):
        unity_client.get_frontend_port_total_byte_rate.return_value = self.test_string
        obj = unity_impl.FrontendPortTotalBandwidth.FrontendPortTotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_total_byte_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_total_byte_rate_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortTotalBandwidth.FrontendPortTotalBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_read_byte_rate(self, unity_client):
        unity_client.get_frontend_port_read_byte_rate.return_value = self.test_string
        obj = unity_impl.FrontendPortReadBandwidth.FrontendPortReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_read_byte_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_read_byte_rate_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortReadBandwidth.FrontendPortReadBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_write_byte_rate(self, unity_client):
        unity_client.get_frontend_port_write_byte_rate.return_value = self.test_string
        obj = unity_impl.FrontendPortWriteBandwidth.FrontendPortWriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_write_byte_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_write_byte_rate_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = unity_impl.FrontendPortWriteBandwidth.FrontendPortWriteBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    # backendPortTable
    @patches.unity_client
    def test_backend_port_id(self, unity_client):
        obj = unity_impl.BackendPortId.BackendPortId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_backend_port_id_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortId.BackendPortIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_name(self, unity_client):
        unity_client.get_backend_port_name.return_value = self.test_string
        obj = unity_impl.BackendPortName.BackendPortName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_backend_port_name_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortName.BackendPortNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_type(self, unity_client):
        unity_client.get_backend_port_type.return_value = self.test_string
        obj = unity_impl.BackendPortType.BackendPortType()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_type.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_backend_port_type_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortType.BackendPortTypeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_port_number(self, unity_client):
        unity_client.get_backend_port_port_number.return_value = self.test_string
        obj = unity_impl.BackendPortPortNumber.BackendPortPortNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_port_number.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_port_number_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortPortNumber.BackendPortPortNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_current_speed(self, unity_client):
        unity_client.get_backend_port_current_speed.return_value = self.test_string
        obj = unity_impl.BackendPortCurrentSpeed.BackendPortCurrentSpeed()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_current_speed.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_current_speed_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortCurrentSpeed.BackendPortCurrentSpeedColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_parent_io_module(self, unity_client):
        unity_client.get_backend_port_parent_io_module.return_value = self.test_string
        obj = unity_impl.BackendPortParentIoModule.BackendPortParentIoModule()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_parent_io_module.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_parent_io_module_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortParentIoModule.BackendPortParentIoModuleColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_parent_sp(self, unity_client):
        unity_client.get_backend_port_parent_sp.return_value = self.test_string
        obj = unity_impl.BackendPortParentStorageProcessor.BackendPortParentStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_parent_sp.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_parent_sp_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortParentStorageProcessor.BackendPortParentStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_status(self, unity_client):
        unity_client.get_backend_port_health_status.return_value = self.test_string
        obj = unity_impl.BackendPortStatus.BackendPortStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_health_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_status_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortStatus.BackendPortStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_total_iops(self, unity_client):
        unity_client.get_backend_port_total_iops.return_value = self.test_string
        obj = unity_impl.BackendPortTotalThroughput.BackendPortTotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_total_iops.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_total_iops_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortTotalThroughput.BackendPortTotalThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_read_iops(self, unity_client):
        unity_client.get_backend_port_read_iops.return_value = self.test_string
        obj = unity_impl.BackendPortReadThroughput.BackendPortReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_read_iops.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_read_iops_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortReadThroughput.BackendPortReadThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_write_iops(self, unity_client):
        unity_client.get_backend_port_write_iops.return_value = self.test_string
        obj = unity_impl.BackendPortWriteThroughput.BackendPortWriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_write_iops.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_write_iops_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortWriteThroughput.BackendPortWriteThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_total_byte_rate(self, unity_client):
        unity_client.get_backend_port_total_byte_rate.return_value = self.test_string
        obj = unity_impl.BackendPortTotalBandwidth.BackendPortTotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_total_byte_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_total_byte_rate_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortTotalBandwidth.BackendPortTotalBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_read_byte_rate(self, unity_client):
        unity_client.get_backend_port_read_byte_rate.return_value = self.test_string
        obj = unity_impl.BackendPortReadBandwidth.BackendPortReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_read_byte_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_read_byte_rate_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortReadBandwidth.BackendPortReadBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_write_byte_rate(self, unity_client):
        unity_client.get_backend_port_write_byte_rate.return_value = self.test_string
        obj = unity_impl.BackendPortWriteBandwidth.BackendPortWriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_write_byte_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_write_byte_rate_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = unity_impl.BackendPortWriteBandwidth.BackendPortWriteBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    # hostTable
    @patches.unity_client
    def test_host_name(self, unity_client):
        obj = unity_impl.HostName.HostName()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_host_name_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = unity_impl.HostName.HostNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    @patches.unity_client
    def test_host_network_address(self, unity_client):
        unity_client.get_host_network_address.return_value = self.test_string
        obj = unity_impl.HostNetworkAddress.HostNetworkAddress()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_host_network_address.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_host_network_address_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = unity_impl.HostNetworkAddress.HostNetworkAddressColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    @patches.unity_client
    def test_host_initiators(self, unity_client):
        unity_client.get_host_initiators.return_value = self.test_string
        obj = unity_impl.HostInitiators.HostInitiators()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_host_initiators.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_host_initiators_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = unity_impl.HostInitiators.HostInitiatorsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    @patches.unity_client
    def test_host_os_version(self, unity_client):
        unity_client.get_host_os_type.return_value = self.test_string
        obj = unity_impl.HostOperationSystemVersion.HostOperationSystemVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_host_os_type.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_host_os_version_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = unity_impl.HostOperationSystemVersion.HostOperationSystemVersionColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    @patches.unity_client
    def test_host_assigned_volumes(self, unity_client):
        unity_client.get_host_assigned_volumes.return_value = self.test_string
        obj = unity_impl.HostAssignedStorageVolumes.HostAssignedStorageVolumes()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_host_assigned_volumes.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_host_assigned_volumes_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = unity_impl.HostAssignedStorageVolumes.HostAssignedStorageVolumesColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    # enclosureTable
    @patches.unity_client
    def test_enclosure_name(self, unity_client):
        unity_client.get_enclosure_name.return_value = self.test_string
        obj = unity_impl.EnclosureName.EnclosureName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_enclosure_name_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosureName.EnclosureNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_model(self, unity_client):
        unity_client.get_enclosure_model.return_value = self.test_string
        obj = unity_impl.EnclosureModel.EnclosureModel()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_model.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_enclosure_model_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosureModel.EnclosureModelColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_serial_number(self, unity_client):
        unity_client.get_enclosure_serial_number.return_value = self.test_string
        obj = unity_impl.EnclosureSerialNumber.EnclosureSerialNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_serial_number.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_serial_number_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosureSerialNumber.EnclosureSerialNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_part_number(self, unity_client):
        unity_client.get_enclosure_part_number.return_value = self.test_string
        obj = unity_impl.EnclosurePartNumber.EnclosurePartNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_part_number.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_part_number_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosurePartNumber.EnclosurePartNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_health_status(self, unity_client):
        unity_client.get_enclosure_health_status.return_value = self.test_string
        obj = unity_impl.EnclosureHealthStatus.EnclosureHealthStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_health_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_health_status_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosureHealthStatus.EnclosureHealthStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_current_power(self, unity_client):
        unity_client.get_enclosure_current_power.return_value = self.test_string
        obj = unity_impl.EnclosureCurrentPower.EnclosureCurrentPower()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_current_power.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_current_power_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosureCurrentPower.EnclosureCurrentPowerColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_avg_power(self, unity_client):
        unity_client.get_enclosure_avg_power.return_value = self.test_string
        obj = unity_impl.EnclosureAveragePower.EnclosureAveragePower()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_avg_power.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_enclosure_avg_power_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosureAveragePower.EnclosureAveragePowerColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_max_power(self, unity_client):
        unity_client.get_enclosure_max_power.return_value = self.test_string
        obj = unity_impl.EnclosureMaxPower.EnclosureMaxPower()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_max_power.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_enclosure_max_power_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosureMaxPower.EnclosureMaxPowerColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_current_temperature(self, unity_client):
        unity_client.get_enclosure_current_temperature.return_value = self.test_string
        obj = unity_impl.EnclosureCurrentTemperature.EnclosureCurrentTemperature()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_current_temperature.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_current_temperature_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosureCurrentTemperature.EnclosureCurrentTemperatureColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_avg_temperature(self, unity_client):
        unity_client.get_enclosure_avg_temperature.return_value = self.test_string
        obj = unity_impl.EnclosureAverageTemperature.EnclosureAverageTemperature()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_avg_temperature.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_avg_temperature_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosureAverageTemperature.EnclosureAverageTemperatureColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_max_temperature(self, unity_client):
        unity_client.get_enclosure_max_temperature.return_value = self.test_string
        obj = unity_impl.EnclosureMaxTemperature.EnclosureMaxTemperature()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_max_temperature.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_max_temperature_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = unity_impl.EnclosureMaxTemperature.EnclosureMaxTemperatureColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    # powerSupplyTable
    @patches.unity_client
    def test_power_supply_name(self, unity_client):
        obj = unity_impl.PowerSupplyName.PowerSupplyName()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_power_supply_name_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = unity_impl.PowerSupplyName.PowerSupplyNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_manufacturer(self, unity_client):
        unity_client.get_power_supply_manufacturer.return_value = self.test_string
        obj = unity_impl.PowerSupplyManufacturer.PowerSupplyManufacturer()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_manufacturer.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_power_supply_manufacturer_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = unity_impl.PowerSupplyManufacturer.PowerSupplyManufacturerColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_model(self, unity_client):
        unity_client.get_power_supply_model.return_value = self.test_string
        obj = unity_impl.PowerSupplyModel.PowerSupplyModel()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_model.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_power_supply_model_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = unity_impl.PowerSupplyModel.PowerSupplyModelColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_firmware_version(self, unity_client):
        unity_client.get_power_supply_firmware_version.return_value = self.test_string
        obj = unity_impl.PowerSupplyFirmwareVersion.PowerSupplyFirmwareVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_firmware_version.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_power_supply_firmware_version_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = unity_impl.PowerSupplyFirmwareVersion.PowerSupplyFirmwareVersionColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_parent_enclosure(self, unity_client):
        unity_client.get_power_supply_parent_enclosure.return_value = self.test_string
        obj = unity_impl.PowerSupplyParentEnclosure.PowerSupplyParentEnclosure()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_parent_enclosure.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_power_supply_parent_enclosure_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = unity_impl.PowerSupplyParentEnclosure.PowerSupplyParentEnclosureColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_sp(self, unity_client):
        unity_client.get_power_supply_sp.return_value = self.test_string
        obj = unity_impl.PowerSupplyStorageProcessor.PowerSupplyStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_sp.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_power_supply_sp_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = unity_impl.PowerSupplyStorageProcessor.PowerSupplyStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_status(self, unity_client):
        unity_client.get_power_supply_health_status.return_value = self.test_string
        obj = unity_impl.PowerSupplyHealthStatus.PowerSupplyHealthStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_health_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_power_supply_status_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = unity_impl.PowerSupplyHealthStatus.PowerSupplyHealthStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    # fanTable
    @patches.unity_client
    def test_fan_name(self, unity_client):
        obj = unity_impl.FanName.FanName()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_fan_name_column(self, unity_client):
        unity_client.get_fans.return_value = self.test_list
        obj = unity_impl.FanName.FanNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_fans.assert_called_once()

    @patches.unity_client
    def test_fan_slot_number(self, unity_client):
        unity_client.get_fan_slot_number.return_value = self.test_string
        obj = unity_impl.FanSlotNumber.FanSlotNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_fan_slot_number.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_fan_slot_number_column(self, unity_client):
        unity_client.get_fans.return_value = self.test_list
        obj = unity_impl.FanSlotNumber.FanSlotNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_fans.assert_called_once()

    @patches.unity_client
    def test_fan_parent_enclosure(self, unity_client):
        unity_client.get_fan_parent_enclosure.return_value = self.test_string
        obj = unity_impl.FanParentEnclosure.FanParentEnclosure()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_fan_parent_enclosure.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_fan_parent_enclosure_column(self, unity_client):
        unity_client.get_fans.return_value = self.test_list
        obj = unity_impl.FanParentEnclosure.FanParentEnclosureColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_fans.assert_called_once()

    @patches.unity_client
    def test_fan_status(self, unity_client):
        unity_client.get_fan_health_status.return_value = self.test_string
        obj = unity_impl.FanHealthStatus.FanHealthStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_fan_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_fan_status_column(self, unity_client):
        unity_client.get_fans.return_value = self.test_list
        obj = unity_impl.FanHealthStatus.FanHealthStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_fans.assert_called_once()

    # BBUTable
    @patches.unity_client
    def test_bbu_name(self, unity_client):
        obj = unity_impl.BbuName.BbuName()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_bbu_name_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = unity_impl.BbuName.BbuNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_manufacturer(self, unity_client):
        unity_client.get_bbu_manufacturer.return_value = self.test_string
        obj = unity_impl.BbuManufacturer.BbuManufacturer()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_manufacturer.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_manufacturer_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = unity_impl.BbuManufacturer.BbuManufacturerColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_model(self, unity_client):
        unity_client.get_bbu_model.return_value = self.test_string
        obj = unity_impl.BbuModel.BbuModel()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_model.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_model_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = unity_impl.BbuModel.BbuModelColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_firmware_version(self, unity_client):
        unity_client.get_bbu_firmware_version.return_value = self.test_string
        obj = unity_impl.BbuFirmwareVersion.BbuFirmwareVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_firmware_version.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_firmware_version_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = unity_impl.BbuFirmwareVersion.BbuFirmwareVersionColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_parent_sp(self, unity_client):
        unity_client.get_bbu_parent_sp.return_value = self.test_string
        obj = unity_impl.BbuParentStorageProcessor.BbuParentStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_parent_sp.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_parent_sp_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = unity_impl.BbuParentStorageProcessor.BbuParentStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_status(self, unity_client):
        unity_client.get_bbu_health_status.return_value = self.test_string
        obj = unity_impl.BbuHealthStatus.BbuHealthStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_status_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = unity_impl.BbuHealthStatus.BbuHealthStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()
