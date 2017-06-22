from datetime import datetime

class VolumeFastCacheReadHitIOs(object):
    def get_value(self):
        return "[%s]  VolumeFastCacheReadHitIOs" % str(datetime.now())