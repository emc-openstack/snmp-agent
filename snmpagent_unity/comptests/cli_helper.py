from snmpagent_unity.comptests import utils
from snmpagent_unity import access
import os
import logging

LOG = logging.getLogger(__name__)


class Helper(object):
    def __init__(self, conf_file=None):
        if not conf_file:
            conf_file = os.path.join(os.path.dirname(__file__), 'agent.conf')
        self.conf_file = conf_file

    @utils.cli_executor
    def add_user(self, name, auth, auth_key, private=None, private_key=None):
        cmd = ['add-user', '--name', name, '--auth', auth, '--auth_key',
               auth_key]
        if private:
            cmd.extend(['--priv', private])
        if private_key:
            cmd.extend(['--priv_key', private_key])
        return cmd

    @utils.cli_executor
    def update_user(self, name, auth, auth_key, private=None,
                    private_key=None):
        cmd = ['update-user', '--name', name, '--auth', auth, '--auth_key',
               auth_key]
        if private:
            cmd.extend(['--priv', private])
        if private_key:
            cmd.extend(['--priv_key', private_key])
        return cmd

    @utils.cli_executor
    def delete_user(self, name):
        return ['delete-user', '--name', name]

    @utils.cli_executor
    def create_community(self, name):
        return ['create-community', '--name', name]

    @utils.cli_executor
    def delete_community(self, name):
        return ['delete-community', '--name', name]

    @utils.cli_executor
    def list_users(self):
        return ['list-users']

    @utils.cli_executor
    def encrypt(self, conf_file=None):
        if not conf_file:
            conf_file = self.conf_file
        return ['encrypt', '--conf_file', conf_file]

    @utils.cli_executor
    def decrypt(self, conf_file=None):
        if not conf_file:
            conf_file = self.conf_file
        return ['decrypt', '--conf_file', conf_file]

    @utils.cli_executor
    def start_service(self):
        return ['start', '--conf_file', self.conf_file]

    @utils.cli_executor
    def stop_service(self):
        return ['stop']

    @utils.cli_executor
    def restart_service(self):
        return ['restart', '--conf_file', self.conf_file]

    @classmethod
    def clear_access_data(cls):
        if os.path.exists(access.get_access_data_path()):
            os.remove(access.get_access_data_path())
