class StorageProcessorFastCacheReadHitIOs(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_sp_fast_cache_read_hits(idx_name)


class StorageProcessorFastCacheReadHitIOsColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_sps()
