class HostAssignedStorageVolumes(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_host_assigned_volumes(idx_name)


class HostAssignedStorageVolumesColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_hosts()
