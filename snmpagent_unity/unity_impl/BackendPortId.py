class BackendPortId(object):
    def read_get(self, name, idx_name, unity_client):
        return idx_name


class BackendPortIdColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_backend_ports()
