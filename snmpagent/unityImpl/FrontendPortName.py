class FrontendPortName(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_frontend_port_name(idx_name)


class FrontendPortNameColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_frontend_ports()
