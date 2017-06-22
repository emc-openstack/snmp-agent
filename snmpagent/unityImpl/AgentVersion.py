from datetime import datetime

class AgentVersion(object):
    def read_get(self, name, idx, storage_context):
        return '[%s] Agent Version for %s: v2.0' % (str(datetime.now()), storage_context.spa)