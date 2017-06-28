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

    # hostTable
    def get_hosts(self):
        return [host.name for host in self.unity_system.get_host()]

    def get_host_network_address(self, host_name):
        host = self.unity_system.get_host(name=host_name)
        # if hasattr(host, 'ip_list'):
        #     return ', '.join(host.ip_list)
        # else:
        #     # TODO: 0x is returned, why?
        #     return '--'
        return ', '.join(host.ip_list) if host.ip_list else '--'

    def get_host_initiators(self, host_name):
        host = self.unity_system.get_host(name=host_name)
        initiators = []
        if host.iscsi_host_initiators:
            initiators.extend(x.initiator_id for x in host.iscsi_host_initiators)
        if host.fc_host_initiators:
            initiators.extend(x.initiator_id for x in host.fc_host_initiators)
        return ', '.join(initiators) if initiators else '--'

    def get_host_os_type(self, host_name):
        host = self.unity_system.get_host(name=host_name)
        return host.os_type if host.os_type else '--'

    def get_host_assigned_volumes(self, host_name):
        host = self.unity_system.get_host(name=host_name)
        # if host.host_luns:
        #     return ', '.join(x.lun.name for x in host.host_luns)
        # else:
        #     return '--'
        return ', '.join(x.lun.name for x in host.host_luns) if host.host_luns else '--'

    def get_volume_fast_cache_read_hit_ios(self):
        return 'volume1'