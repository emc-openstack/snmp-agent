class DiskUtilization(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_utilization(idx_name)


class DiskUtilizationColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
