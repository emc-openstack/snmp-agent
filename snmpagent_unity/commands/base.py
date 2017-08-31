import docopt
from snmpagent_unity import utils


class BaseCommand(object):
    """Base class for the commands"""
    name = 'base-command'

    # Flag whether to log to stdout when log file path is not set.
    log_to_stdout = True

    def __init__(self, cmd_args, global_args):
        """ Initialize the commands.

        :param cmd_args: arguments of the command
        :param global_args: arguments of the program
        """
        self.args = docopt.docopt(self.__doc__, argv=cmd_args)
        self.global_args = global_args
        utils.setup_log(log_file_path=self.global_args['--log_file'],
                        level=self.global_args['--log_level'],
                        log_to_stdout=self.log_to_stdout)

    def do(self):
        """Execute the commands"""
        raise NotImplementedError()
