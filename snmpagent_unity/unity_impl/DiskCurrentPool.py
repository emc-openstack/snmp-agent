class DiskCurrentPool(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_current_pool(idx_name)


class DiskCurrentPoolColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
