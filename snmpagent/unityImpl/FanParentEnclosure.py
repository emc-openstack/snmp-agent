class FanParentEnclosure(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_fan_parent_enclosure(idx_name)


class FanParentEnclosureColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_fans()
