import logging
import sys
from logging import handlers

import docopt


def _setup_logger(log_file_path=None, level=None, log_to_stdout=True):
    level = logging.INFO if level is None else level
    logging.basicConfig(
        level=level,
        format='%(asctime)-15s %(name)-12s %(levelname)-8s %(message)s')
    handler = None
    if log_file_path is None:
        if log_to_stdout:
            handler = logging.StreamHandler(stream=sys.stdout)
    else:
        handler = handlers.RotatingFileHandler(log_file_path,
                                               maxBytes=100 * (2 ** 20),
                                               backupCount=5)
    if handler is not None:
        logging.getLogger('').addHandler(handler)


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
        _setup_logger(self.global_args['--log_file'],
                      self.global_args['--log_level'], self.log_to_stdout)

    def do(self):
        """Execute the commands"""
        raise NotImplementedError()
