class HostId(object):
    def read_get(self, name, idx_name, unity_client):
        return idx_name


class HostIdColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_hosts()
