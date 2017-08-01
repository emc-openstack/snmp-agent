class VolumeFastCacheReadHitRate(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_fast_cache_read_hit_rate(idx_name)


class VolumeFastCacheReadHitRateColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
