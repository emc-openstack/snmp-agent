class FrontendPortTotalThroughput(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_frontend_port_total_iops(idx_name)


class FrontendPortTotalThroughputColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_frontend_ports()
