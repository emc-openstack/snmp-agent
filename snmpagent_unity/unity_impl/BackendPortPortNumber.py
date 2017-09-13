class BackendPortPortNumber(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_backend_port_port_number(idx_name)


class BackendPortPortNumberColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_backend_ports()
