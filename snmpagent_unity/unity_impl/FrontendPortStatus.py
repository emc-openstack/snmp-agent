class FrontendPortStatus(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_frontend_port_health_status(idx_name)


class FrontendPortStatusColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_frontend_ports()
