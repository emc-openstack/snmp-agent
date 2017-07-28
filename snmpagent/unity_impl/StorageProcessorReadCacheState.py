class StorageProcessorReadCacheState(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_sp_block_cache_read_hit_ratio(idx_name)


class StorageProcessorReadCacheStateColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_sps()
