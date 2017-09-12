class VolumeWriteBandwidth(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_write_byte_rate(idx_name)


class VolumeWriteBandwidthColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
