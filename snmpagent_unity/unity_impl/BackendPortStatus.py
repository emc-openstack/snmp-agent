class BackendPortStatus(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_backend_port_health_status(idx_name)


class BackendPortStatusColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_backend_ports()
