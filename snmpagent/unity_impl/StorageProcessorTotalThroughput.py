class StorageProcessorTotalThroughput(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_sp_block_total_iops(idx_name)


class StorageProcessorTotalThroughputColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_sps()
