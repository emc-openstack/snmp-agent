from datetime import datetime

class volumeFastCacheReadHitIOs(object):
    def get_value(self, name, idx):
        return "[%s]  VolumeFastCacheReadHitIOs" % str(datetime.now())
