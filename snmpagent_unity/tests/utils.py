import os


def conf_full_path(conf_file_name):
    return os.path.join(os.path.dirname(__file__), 'test_data', 'configs',
                        conf_file_name)


def unity_data(category, data_file):
    return os.path.join(os.path.dirname(__file__), 'test_data', 'unity',
                        category, data_file)
