class FrontendPortReadThroughput(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_frontend_port_read_iops(idx_name)


class FrontendPortReadThroughputColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_frontend_ports()
