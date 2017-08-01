class VolumeTotalBandwidth(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_total_byte_rate(idx_name)


class VolumeTotalBandwidthColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
