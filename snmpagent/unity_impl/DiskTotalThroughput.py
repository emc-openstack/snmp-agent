class DiskTotalThroughput(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_total_iops(idx_name)


class DiskTotalThroughputColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
