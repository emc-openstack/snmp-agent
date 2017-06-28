from storops import UnitySystem


class CachedUnityClientManager(object):
    def __init__(self):
        self._cache = {}

    def get_unity_client(self, name, *args):
        if name not in self._cache:
            unity_client = UnityClient(*args)
            self._cache[name] = unity_client
        else:
            unity_client = self._cache[name]
        return unity_client


class UnityClient(object):
    manager = CachedUnityClientManager()

    def __init__(self, host=None, username=None, password=None, port=443):
        self.unity_system = UnitySystem(host=host, username=username, password=password, port=port)

    @classmethod
    def get_unity_client(cls, name, *args):
        return cls.manager.get_unity_client(name, *args)

    # system
    def get_agent_version(self):
        return "1.0"

    def get_mib_version(self):
        return "1.0"

    def get_manufacturer(self):
        return "DellEMC"

    def get_model(self):
        return self.unity_system.model

    def get_serial_number(self):
        return self.unity_system.serial_number

    def get_operation_environment_version(self):
        return self.unity_system.system_version

    def get_management_ip(self):
        pass

    def get_current_power(self):
        # TODO: failed to snmpget currentPower
        return self.unity_system.current_power

    def get_average_power(self):
        return self.unity_system.average_power

    def get_number_of_storage_processor(self):
        return len(self.unity_system.get_sp())

    def get_number_of_enclosure(self):
        pass

    # storageProcessorTable
    def get_sps(self):
        return [pool.name for pool in self.unity_system.get_sp()]

    def get_sp_serial_number(self, name):
        sp = self.unity_system.get_sp(name=name)
        return sp.emc_serial_number

    def get_sp_health_status(self, name):
        sp = self.unity_system.get_sp(name=name)
        return sp.health.value.name

    # poolTable
    def get_pools(self):
        return [pool.name for pool in self.unity_system.get_pool()]

    # def get_pool_disk_types(self, name):
    #     pool = self.unity_system.get_pool(name=name)
    #     return

    def get_pool_raid_levels(self, name):
        pool = self.unity_system.get_pool(name=name)
        return pool.raid_type.name

    def get_pool_fast_cache_status(self, name):
        pool = self.unity_system.get_pool(name=name)
        return str(pool.is_fast_cache_enabled)

    # def get_pool_number_of_disk(self, name):
    #     pool = self.unity_system.get_pool(name=name)
    #     return

    def get_pool_size_total(self, name):
        pool = self.unity_system.get_pool(name=name)
        return str(pool.size_total)

    def get_pool_size_free(self, name):
        pool = self.unity_system.get_pool(name=name)
        return str(pool.size_free)

    def get_pool_size_used(self, name):
        pool = self.unity_system.get_pool(name=name)
        return str(pool.size_used)

    # def get_pool_size_ultilization(self, name):
    #     pool = self.unity_system.get_pool(name=name)
    #     return

    # diskTable
    def get_disks(self):
        return [disk.name for disk in self.unity_system.get_disk()]

    def get_disk_model(self, name):
        disk = self.unity_system.get_disk(name=name)
        return disk.model

    def get_disk_serial_number(self, name):
        disk = self.unity_system.get_disk(name=name)
        return disk.emc_serial_number

    def get_disk_version(self, name):
        disk = self.unity_system.get_disk(name=name)
        return disk.version

    def get_disk_type(self, name):
        disk = self.unity_system.get_disk(name=name)
        if disk.disk_technology:
            return disk.disk_technology.name
        else:
            return

    def get_disk_health_status(self, name):
        disk = self.unity_system.get_disk(name=name)
        return disk.health.value.name

    def get_disk_raw_size(self, name):
        disk = self.unity_system.get_disk(name=name)
        return str(disk.raw_size)

    def get_disk_current_pool(self, name):
        disk = self.unity_system.get_disk(name=name)
        if disk.pool:
            return disk.pool.name
        else:
            return

    # hostTable
    def get_hosts(self):
        return [host.name for host in self.unity_system.get_host()]

    def get_host_network_address(self, name):
        host = self.unity_system.get_host(name=name)
        return ', '.join(host.ip_list)

    def get_host_initiators(self, name):
        host = self.unity_system.get_host(name=name)
        initiators = []
        if host.iscsi_host_initiators:
            initiators.extend(x.initiator_id for x in host.iscsi_host_initiators)
        if host.fc_host_initiators:
            initiators.extend(x.initiator_id for x in host.fc_host_initiators)
        return ', '.join(initiators)

    def get_host_os_type(self, name):
        host = self.unity_system.get_host(name=name)
        return host.os_type

    def get_host_assigned_volumes(self, name):
        host = self.unity_system.get_host(name=name)
        if host.host_luns:
            return ', '.join(x.lun.name for x in host.host_luns)
        else:
            return
