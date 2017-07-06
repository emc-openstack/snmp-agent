class FrontendPortId(object):
    def read_get(self, name, idx_name, unity_client):
        # return idx_name
        return unity_client.get_frontend_port_id(idx_name)


class FrontendPortIdColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_frontend_ports()
