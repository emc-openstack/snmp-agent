class VolumeWriteThroughput(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_write_iops(idx_name)


class VolumeWriteThroughputColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
