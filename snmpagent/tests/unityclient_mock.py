import json

from snmpagent.clients import UnityClient


def camel_to_underline(camel_format):
    underline_format = ''
    if isinstance(camel_format, str):
        for _s_ in camel_format:
            underline_format += _s_ if _s_.islower() else '_' + _s_.lower()
    return underline_format


def underline_to_camel(underline_format):
    camel_format = ''
    if isinstance(underline_format, str):
        for _s_ in underline_format.split('_'):
            camel_format += _s_.capitalize()
    return camel_format


class Data(object):
    def __init__(self, content):
        for k, v in content.items():
            if isinstance(v, dict):
                setattr(self, camel_to_underline(k), Data(v))
                print('test')
            else:
                setattr(self, camel_to_underline(k), v)


class MockUnityClient(UnityClient):
    def __init__(self, data_file):
        self.unity_system = self
        self.data_file = data_file
        self.path_disk = None

    def _get_data(self, name=None):
        with open(self.path_disk, 'r') as f:
            data = json.load(f)

        obj_list = []
        for item in data['entries']:
            obj_list.append(Data(content=item['content']))

        if name is None:
            return obj_list
        else:
            obj = [obj for obj in obj_list if obj.name == name][0]
            return obj

    def get_disk(self, name=None):
        self.path_disk = self.data_file
        return self._get_data(name=name)

    def get_battery(self, name=None):
        self.path_disk = self.data_file
        return self._get_data(name=name)


if __name__ == '__main__':
    # mock = MockUnityClient()
    # mock.get_datas()
    # print(mock.unity_system.get_disk(name='DAE 0 1 Disk 0'))
    mock = MockUnityClient('.\\unity\\battery\\battery_positive.json')
    print(mock.unity_system.get_battery(name='SP A Battery 0'))
    print(mock.unity_system.get_bbu_parent_sp(name='SP A Battery 0'))
