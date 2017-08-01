class DiskWriteThroughput(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_write_iops(idx_name)


class DiskWriteThroughputColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
