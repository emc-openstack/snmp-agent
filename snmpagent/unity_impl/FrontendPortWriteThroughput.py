class FrontendPortWriteThroughput(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_frontend_port_write_iops(idx_name)


class FrontendPortWriteThroughputColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_frontend_ports()
