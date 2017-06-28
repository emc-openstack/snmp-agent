from datetime import datetime

class VolumeFastCacheReadHitIOs(object):
    def read_get(self, name, idx, unity_client):
        return "[%s] %s" % (str(datetime.now()), unity_client.get_volume_fast_cache_read_hit_ios())


class VolumeFastCacheReadHitIOsColumn(object):
    def get_idx(self, name, idx, unity_client):
        return "[%s] %s" % (str(datetime.now()), unity_client.get_volume_fast_cache_read_hit_ios())
