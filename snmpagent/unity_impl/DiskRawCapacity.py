class DiskRawCapacity(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_raw_size(idx_name)


class DiskRawCapacityColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
