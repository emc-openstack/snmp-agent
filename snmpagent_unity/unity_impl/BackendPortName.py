class BackendPortName(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_backend_port_name(idx_name)


class BackendPortNameColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_backend_ports()
