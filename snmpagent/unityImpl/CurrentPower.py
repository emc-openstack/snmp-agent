from datetime import datetime

class CurrentPower(object):
    def read_get(self, name, idx, storage_context):
        return '[%s] CurrentPower for %s' % (str(datetime.now()), storage_context.spa)