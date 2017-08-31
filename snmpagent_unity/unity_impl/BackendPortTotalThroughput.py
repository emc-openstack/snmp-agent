class BackendPortTotalThroughput(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_backend_port_total_iops(idx_name)


class BackendPortTotalThroughputColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_backend_ports()
