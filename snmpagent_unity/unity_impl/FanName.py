class FanName(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_fan_name(idx_name)


class FanNameColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_fans()
