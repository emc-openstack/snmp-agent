from datetime import datetime

class VolumeFastCacheReadHitIOs(object):
    def read_get(self, name, idx, storage_context):
        return "[%s]  VolumeFastCacheReadHitIOs from %s" % (str(datetime.now()), storage_context.spb)
