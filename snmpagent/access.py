import os

from snmpagent import config, enums, utils
from snmpagent import exceptions as snmp_ex


def _validate_params(security_level, auth_protocol=None, auth_key=None,
                     priv_protocol=None, priv_key=None):
    level = utils.enum(enums.SecurityLevel, security_level)
    if level is None:
        raise snmp_ex.UserConfigError(
            'Not supported security level: {}'.format(security_level))

    auth_p, auth_k = None, None
    priv_p, priv_k = None, None
    if level != enums.SecurityLevel.NO_AUTH_NO_PRIV:
        auth_p = utils.enum(enums.AuthProtocol, auth_protocol)
        if auth_p is None:
            raise snmp_ex.UserConfigError(
                'Not supported auth protocol: {}'.format(auth_protocol))
        auth_k = auth_key

        if level == enums.SecurityLevel.AUTH_PRIV:
            priv_p = utils.enum(enums.PrivProtocol, priv_protocol)
            if priv_p is None:
                raise snmp_ex.UserConfigError(
                    'Not supported priv protocol: {}'.format(priv_protocol))
            priv_k = priv_key
    return level, auth_p, auth_k, priv_p, priv_k


def _get_conf_file_path():
    return os.path.join(os.path.dirname(__file__), 'configs', 'access.conf')


CONF_FILE_PATH = _get_conf_file_path()


class Access(object):
    def __init__(self):
        self.user_conf = config.UserConfig(CONF_FILE_PATH)

    def add_v3_user(self, name, security_level, auth_protocol=None,
                    auth_key=None, priv_protocol=None, priv_key=None):
        if name in self.user_conf.entries:
            raise snmp_ex.UserExistingError(
                'The user: {} already exists.'.format(name))

        level, auth_p, auth_k, priv_p, priv_k = _validate_params(
            security_level, auth_protocol, auth_key, priv_protocol, priv_key)

        self.user_conf.entries[name] = config.UserV3ConfigEntry(
            name, None, level, auth_p, auth_k, priv_p, priv_k)
        self.user_conf.save()

    def add_v2_user(self, name):
        if name in self.user_conf.entries:
            raise snmp_ex.UserExistingError(
                'The user: {} already exists.'.format(name))

        self.user_conf.entries[name] = config.UserV2ConfigEntry(
            name, enums.Community.PUBLIC)
        self.user_conf.save()

    def delete_v3_user(self, name):
        if name not in self.user_conf.entries:
            return
        del self.user_conf.entries[name]
        self.user_conf.save()

    def delete_v2_user(self, name):
        if name not in self.user_conf.entries:
            return
        del self.user_conf.entries[name]
        self.user_conf.save()

    def update_v3_user(self, name, security_level=None, auth_protocol=None,
                       auth_key=None, priv_protocol=None, priv_key=None):
        if name not in self.user_conf.entries:
            # TODO log message if needed
            return
        old = self.user_conf.entries[name]
        security_level = (old.security_level if security_level is None
                          else security_level)
        auth_protocol = (old.auth_protocol if auth_protocol is None
                         else auth_protocol)
        auth_key = old.auth_key.raw if auth_key is None else auth_key
        priv_protocol = (old.priv_protocol if priv_protocol is None
                         else priv_protocol)
        priv_key = old.priv_key.raw if priv_key is None else priv_key
        level, auth_p, auth_k, priv_p, priv_k = _validate_params(
            security_level, auth_protocol, auth_key, priv_protocol, priv_key)
        self.user_conf.entries[name] = config.UserV3ConfigEntry(
            name, None, level, auth_p, auth_k, priv_p, priv_k)
        self.user_conf.save()

    def list_users(self):
        v2, v3 = config.UserConfig.split_v2_v3(self.user_conf.entries)
        print('\n'.join([config.USER_V2_SHOW_HEAD] +
                        [e.show() for e in v2] +
                        ['\n' + config.USER_V3_SHOW_HEAD] +
                        [e.show() for e in v3]))


access = Access()
