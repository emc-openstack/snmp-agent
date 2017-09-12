class CliException(Exception):
    def __init__(self, command, rc, out, err):
        self.command = command
        self.rc = rc
        self.out = out
        self.err = err
        self.message = "Failed to execute command '{}', out: '{}', " \
                       "err: '{}', rc: '{}'".format(command, rc, out, err)
