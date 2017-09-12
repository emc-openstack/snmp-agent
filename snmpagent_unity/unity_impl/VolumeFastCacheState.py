class VolumeFastCacheState(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_fast_cache_status(idx_name)


class VolumeFastCacheStateColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
