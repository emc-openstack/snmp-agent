class DiskReadBandwidth(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_read_byte_rate(idx_name)


class DiskReadBandwidthColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
