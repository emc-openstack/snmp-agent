from datetime import datetime

class AgentInfo(object):
    def get_agent_version(self, name, idx):
        return '[%s] Agent Version: v2.0' % str(datetime.now())

    def get_mib_version(self, name, idx):
        return '[%s] MIB Version: v1.0' % str(datetime.now())
