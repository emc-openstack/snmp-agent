class BbuParentStorageProcessor(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_bbu_parent_sp(idx_name)


class BbuParentStorageProcessorColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_bbus()
