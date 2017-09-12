class StorageProcessorTotalBandwidth(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_sp_total_byte_rate(idx_name)


class StorageProcessorTotalBandwidthColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_sps()
