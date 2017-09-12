import logging
import sys
from logging import handlers

from snmpagent_unity import exceptions as snmp_ex


def enum(enum_clz, value):
    if isinstance(value, enum_clz):
        return value
    return enum_clz.from_str(value) if value else None


def setup_log(log_file_path='snmpagent-unity.log', level=None,
              log_to_stdout=True, max_bytes=104857600, max_file_count=5):
    if level:
        level = getattr(logging, level.upper(), None)
    else:
        level = logging.INFO

    fmt_str = '%(asctime)-15s %(name)-12s %(threadName)s ' \
              '%(levelname)-8s %(message)s'
    fmt = logging.Formatter(fmt_str)
    # Set root logger to `level` or it would be warning which will
    # suppress logs lower than warning.
    root = logging.getLogger()
    root.setLevel(level)
    if log_to_stdout:
        console = logging.StreamHandler()
        console.setLevel(level)
        console.setFormatter(fmt)
        root.addHandler(console)
    if log_file_path:
        file_handler = handlers.RotatingFileHandler(
            filename=log_file_path,
            maxBytes=0 if not max_bytes else int(max_bytes),
            backupCount=0 if not max_file_count else int(max_file_count))
        file_handler.setLevel(level)
        file_handler.setFormatter(fmt)
        root.addHandler(file_handler)


def log_command_exception(cmd):
    def wrap_exception(*args, **kwargs):
        try:
            r = cmd(*args, **kwargs)
        except snmp_ex.SNMPAgentException as ex:
            sys.stderr.writelines("Failed to execute '{}': {}\n".format(
                args[0].name, ex))
            r = -255
        return r

    return wrap_exception


def log_trace(excType, excValue, traceback):
    logging.error(
        "Got an uncaught exception",
        exc_info=(excType, excValue, traceback))


def disable_urllib3_warnings():
    try:
        import urllib3

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    except:
        pass
