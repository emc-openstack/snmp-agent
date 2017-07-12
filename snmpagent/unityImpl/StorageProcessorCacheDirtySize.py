class StorageProcessorCacheDirtySize(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_sp_cache_dirty_size(idx_name)


class StorageProcessorCacheDirtySizeColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_sps()
