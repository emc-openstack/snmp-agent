from datetime import datetime

class MibVersion(object):
    def read_get(self, name, idx, storage_context):
        return '[%s] Mib Version for %s: v2.0' % (str(datetime.now()), storage_context.spa)