"""
Dell-EMC SNMP agent.

usage:
    snmpagent [-hV --log_file <log_file> --log_level <log_level>] <command> \
[<args>...]

options:
    -h --help               shows the help, could be used for commands.
    -V --version            shows the version.
    --log_file <log_file>   sets the log file path.
    --log_level <log_level> sets the log level.

supported commands:
    add-user                adds a v3 user
    update-user             updates the info of a v3 user
    delete-user             deletes a v3 user
    create-community        creates a v2 community access
    delete-community        deletes a v2 community access
    list-users              lists all users/access
    encrypt                 encrypts the configuration files
    decrypt                 decrypts the configuration files
    start                   starts a snmp agent daemon
    stop                    stops the snmp agent daemon
    restart                 restarts the snmp agent daemon

examples:
    snmpagent --help
    snmpagent add-user --help
"""

import docopt

import snmpagent
from snmpagent import commands


def main():
    """Main cli entry point for distributing cli commands."""
    args = docopt.docopt(__doc__, version=snmpagent.__version__,
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
