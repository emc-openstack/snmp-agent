import logging
import os

import snmpagent_unity

from snmpagent_unity import config, enums, utils
from snmpagent_unity import exceptions as snmp_ex

LOG = logging.getLogger(__name__)


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


def get_access_data_path():
    """Returns the access data location.

       The data location is fixed:
       on Windows, it's %USERPROFILE%\.snmpagent\access.db
       on Linux, it's %HOME%/.snmpagent\access.db

    """
    data_folder = os.path.expanduser(
        "~{}.{}".format(os.path.sep, snmpagent_unity.SERVICE_NAME))
    access_file = os.path.join(data_folder,
                               'access.db')
    # Make the directory
    if not os.path.isdir(data_folder):
        os.mkdir(data_folder)
        LOG.info(
            "Created '{}' for access data persistence.".format(data_folder))
    if not os.path.exists(access_file):
        with open(access_file, 'w'):
            LOG.debug("Created file '{}' for storing access data".format(
                access_file))
    return access_file


class Access(object):
    def __init__(self):
        self.user_conf = config.UserConfig(get_access_data_path())

    def add_v3_user(self, name, security_level, auth_protocol=None,
                    auth_key=None, priv_protocol=None, priv_key=None):
        if name in self.user_conf.entries:
            raise snmp_ex.UserExistingError(
                "The user: '{}' already exists.".format(name))

        level, auth_p, auth_k, priv_p, priv_k = _validate_params(
            security_level, auth_protocol, auth_key, priv_protocol, priv_key)

        self.user_conf.entries[name] = config.UserV3ConfigEntry(
            name, None, level, auth_p, auth_k, priv_p, priv_k)
        self.user_conf.save()
        LOG.info("Added user '{}' successfully.".format(name))

    def add_v2_user(self, name):
        if name in self.user_conf.entries:
            raise snmp_ex.UserExistingError(
                "The user: '{}' already exists.".format(name))

        self.user_conf.entries[name] = config.UserV2ConfigEntry(
            name, name)
        self.user_conf.save()
        LOG.info("Added user '{}' successfully.".format(name))

    def delete_v3_user(self, name):
        if name not in self.user_conf.entries:
            raise snmp_ex.UserNotExistsError(
                "User '{}' was already deleted.".format(name))
        del self.user_conf.entries[name]
        self.user_conf.save()
        LOG.info("Deleted user '{}' successfully.".format(name))

    def delete_v2_user(self, name):
        if name not in self.user_conf.entries:
            raise snmp_ex.UserNotExistsError(
                "User '{}' was already deleted.".format(name))
        del self.user_conf.entries[name]
        self.user_conf.save()
        LOG.info("Deleted user '{}' successfully.".format(name))

    def update_v3_user(self, name, security_level=None, auth_protocol=None,
                       auth_key=None, priv_protocol=None, priv_key=None):
        if name not in self.user_conf.entries:
            raise snmp_ex.UserNotExistsError(
                "Could not update nonexistent user '{}'.".format(name))
        old = self.user_conf.entries[name]

        level, auth_p, auth_k, priv_p, priv_k = _validate_params(
            security_level, auth_protocol, auth_key, priv_protocol, priv_key)
        if old.auth_protocol != auth_p:
            raise snmp_ex.UserInvalidProtocolError(
                "'{}' does not match auth with '{}'.".format(
                    auth_p,
                    old.auth_protocol))

        if old.auth_key.raw != auth_k:
            raise snmp_ex.UserInvalidPasswordError(
                'Incorrect password supplied.')
        self.user_conf.entries[name] = config.UserV3ConfigEntry(
            name, None, level, auth_p, auth_k, priv_p, priv_k)
        self.user_conf.save()
        LOG.info("Updated user '{}' successfully.".format(name))

    def list_users(self):
        v2, v3 = config.UserConfig.split_v2_v3(self.user_conf.entries)
        print('\n'.join([config.USER_V2_SHOW_HEAD] +
                        [str(e) for e in v2] +
                        ['\n' + config.USER_V3_SHOW_HEAD] +
                        [str(e) for e in v3]))
