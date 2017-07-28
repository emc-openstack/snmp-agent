class BackendPortType(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_backend_port_type(idx_name)


class BackendPortTypeColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_backend_ports()
