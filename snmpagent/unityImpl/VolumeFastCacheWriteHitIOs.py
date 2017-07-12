class VolumeFastCacheWriteHitIOs(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_fast_cache_write_hits(idx_name)


class VolumeFastCacheWriteHitIOsColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
