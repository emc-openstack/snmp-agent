class FrontendPortType(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_frontend_port_type(idx_name)


class FrontendPortTypeColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_frontend_ports()
