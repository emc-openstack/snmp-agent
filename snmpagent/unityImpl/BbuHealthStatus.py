class BbuHealthStatus(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_bbu_health_status(idx_name)


class BbuHealthStatusColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_bbus()
