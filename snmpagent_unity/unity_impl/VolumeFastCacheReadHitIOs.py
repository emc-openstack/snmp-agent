class VolumeFastCacheReadHitIOs(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_fast_cache_read_hits(idx_name)


class VolumeFastCacheReadHitIOsColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
