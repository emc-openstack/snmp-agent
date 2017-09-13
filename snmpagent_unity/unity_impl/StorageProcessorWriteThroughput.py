class StorageProcessorWriteThroughput(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_sp_block_write_iops(idx_name)


class StorageProcessorWriteThroughputColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_sps()
