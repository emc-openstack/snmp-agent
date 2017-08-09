import logging
import os

from snmpagent import config as snmp_config


def set_log_config(config_file):
    log_levels = {'critical': logging.CRITICAL,
                  'error': logging.ERROR,
                  'warning': logging.WARNING,
                  'info': logging.INFO,
                  'debug': logging.DEBUG,
                  'all': logging.DEBUG}

    log_level, log_file, log_file_maxbytes, log_file_count = _parse_config(
        config_file)

    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    level = log_levels.get(log_level, logging.INFO)

    handler = logging.handlers.RotatingFileHandler(log_file,
                                                   maxBytes=log_file_maxbytes,
                                                   backupCount=log_file_count)

    logging.basicConfig(level=level,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='[%Y-%m-%d %H:%M:%S]',
                        handlers=(handler,),
                        )

    if log_level == 'all':
        from pysnmp import debug
        debug.setLogger(debug.Debug(log_level, printer=debug.Printer()))


def _parse_config(config_file):
    agent_config = snmp_config.AgentConfig(config_file).entries

    log_level = agent_config.default_section.get('log_level').lower()
    log_file = os.path.abspath(agent_config.default_section.get('log_file'))

    log_file_maxbytes = agent_config.default_section.get('log_file_maxbytes')
    log_file_maxbytes = int(
        log_file_maxbytes) if log_file_maxbytes else 10485760
    log_file_count = agent_config.default_section.get('log_file_count')
    log_file_count = int(log_file_count) if log_file_count else 10

    return log_level, log_file, log_file_maxbytes, log_file_count
