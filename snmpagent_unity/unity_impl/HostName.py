class HostName(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_host_name(idx_name)


class HostNameColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_hosts()
