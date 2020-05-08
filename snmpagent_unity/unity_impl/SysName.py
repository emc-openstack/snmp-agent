class SysName(object):
    def read_get(self, name, idx, unity_client):
        return unity_client.get_system_name()
