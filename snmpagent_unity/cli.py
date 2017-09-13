"""
Dell EMC Unity SNMP Off-Array Agent.

usage:
    snmpagent-unity [-hV] <command> [<args>...]

options:
    -h --help               Show the help, could be used for commands
    -V --version            Show the version

supported commands:
    add-user                Add a v3 user
    update-user             Update the info of a v3 user
    delete-user             Delete a v3 user
    create-community        Create a v2 community access
    delete-community        Delete a v2 community access
    list-users              List all users/access
    encrypt                 Encrypt the configuration files
    decrypt                 Decrypt the configuration files
    start                   Start a SNMP agent daemon
    stop                    Stop the SNMP agent daemon
    restart                 Restart the SNMP agent daemon

examples:
    snmpagent-unity --help
    snmpagent-unity add-user --help
"""

import docopt

import snmpagent_unity
from snmpagent_unity import commands


def main():
    """Main cli entry point for distributing cli commands."""
    args = docopt.docopt(__doc__, version=snmpagent_unity.__version__,
                         options_first=True, help=True)
    cmd_name = args.pop('<command>')
    cmd_args = args.pop('<args>')

    cmd_class = commands.CMD_DICT.get(cmd_name, None)
    if cmd_class is None:
        raise docopt.DocoptExit(
            message="Not supported command: {}".format(cmd_name))

    cmd_args = [cmd_name] + cmd_args
    cmd = cmd_class(cmd_args, args)
    return cmd.do()
