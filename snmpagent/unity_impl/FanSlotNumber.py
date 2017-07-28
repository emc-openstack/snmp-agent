class FanSlotNumber(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_fan_slot_number(idx_name)


class FanSlotNumberColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_fans()
