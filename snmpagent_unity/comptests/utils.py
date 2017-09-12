import functools
import logging
import subprocess
import time
import yaml
import os
import random

import storops

import snmpagent_unity
from snmpagent_unity.comptests import exceptions

LOG = logging.getLogger(__name__)


def parse_conf(yaml_file):
    with open(yaml_file, 'r') as f:
        return yaml.safe_load(f)


def get_env_yaml():
    yaml_file = os.path.join(os.path.dirname(__file__), 'env.yml')
    return parse_conf(yaml_file)


def get_unity_system(unity_conf):
    return storops.UnitySystem(unity_conf['ip'],
                               unity_conf['user'],
                               unity_conf['password'])


def filter_disk_group(disk_groups):
    """Get the disk group with most un-configured disks."""
    dgs = sorted(disk_groups, key=lambda dg: dg.unconfigured_disks,
                 reverse=True)
    return dgs[0]


class Environment(object):
    """Class for storing the unity objects."""

    def __init__(self):
        self.pools = []
        self.luns = []
        self.hosts = []


garbage = Environment()


def create_pool_if_needed():
    env = get_env_yaml()
    pool_num = env['unity']['pools']['min_number']

    unity = get_unity_system(env['unity'])
    pools = unity.get_pool()
    pools = [p for p in pools]
    if len(pools) < pool_num:
        from storops.unity.resource.pool import RaidGroupParameter
        from storops.unity import enums
        LOG.info(
            "Required number of pools is {}, actual is {} ".format(
                pool_num, len(pools)))
        for x in range(pool_num - len(pools)):
            pool_name = "snmp_pool_{}".format(x)
            dg = filter_disk_group(unity.get_disk_group())
            raid_groups = [
                RaidGroupParameter(
                    dg.id, 2, enums.RaidTypeEnum.RAID10,
                    enums.RaidStripeWidthEnum.BEST_FIT)]
            new_pool = unity.create_pool(
                pool_name, raid_groups,
                description='Created for snmpagent-unity testing.')
            LOG.info("Created pool with ID: {}".format(new_pool.id))
            pools.append(new_pool)
            garbage.pools.append(new_pool)

    else:
        LOG.info(
            "There are enough pools, expect={}, "
            "actual={}, skipping creating pools".format(pool_num, len(pools)))
    return pools


def create_lun_if_needed(pools=None):
    env = get_env_yaml()
    lun_num = env['unity']['luns']['min_number']
    unity = get_unity_system(env['unity'])
    luns = unity.get_lun()
    luns = [lun for lun in luns]
    if pools:
        if len(luns) < lun_num:
            LOG.info(
                "Required number of luns is {}, actual "
                "is {}".format(lun_num, len(luns)))
            for x in range(lun_num - len(luns)):
                random.shuffle(pools)
                pool = pools[0]
                lun = pool.create_lun('snmp_lun_{}'.format(x))
                LOG.info("Created lun with ID: {}".format(lun.id))
                luns.append(lun)
                garbage.luns.append(lun)
        else:
            LOG.info(
                "There are enough LUNs, expect={}, "
                "actual={}, skipping creating luns".format(
                    lun_num, len(luns)))

    else:
        LOG.debug("Not creating LUNs, not pool specified.")

    return luns


def create_host_if_needed():
    env = get_env_yaml()
    host_num = env['unity']['hosts']['min_number']
    unity = get_unity_system(env['unity'])
    hosts = unity.get_host()
    hosts = [h for h in hosts]
    if len(hosts) < host_num:
        for x in range(host_num - len(hosts)):
            host = unity.create_host('snmp_host_{}'.format(x))
            LOG.info("Created lun with ID: {}".format(host.id))
            hosts.append(host)
            garbage.hosts.append(host)

    else:
        LOG.info(
            "There are enough hosts, expect={}, "
            "actual={}, skipping creating pools".format(host_num, len(hosts)))
    return hosts


def cleanup_env():
    if garbage:
        if garbage.hosts:
            for h in garbage.hosts:
                LOG.info("Deleting host '{}'".format(h.id))
                h.delete()
        if garbage.luns:
            for l in garbage.luns:
                LOG.info("Deleting lun '{}'".format(l.id))
                l.delete()
        if garbage.pools:
            for p in garbage.pools:
                LOG.info("Deleting pool '{}'".format(p.id))
                p.delete()


def raise_if_error(command, rc, out, err):
    if rc != 0:
        raise exceptions.CliException(command, rc, out, err)


def cli_executor(func):
    @functools.wraps(func)
    def _executor(*args, **kwargs):
        command = func(*args, **kwargs)
        command.insert(0, snmpagent_unity.COMMNAD_NAME)
        start_time = time.time()
        p = subprocess.Popen(command, stdin=None, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        out, err = p.communicate()
        rc = p.returncode
        used = time.time() - start_time
        LOG.debug(
            "Executed command => COMMAND: '{}', OUT: '{}', ERR: '{}', "
            "RC: '{}', TIME: '{}'".format(
                ' '.join(command), out, err, rc, used)
        )
        # raise_if_error(command, rc, out, err)
        return rc

    return _executor


def local_test():
    pools = create_pool_if_needed()
    create_lun_if_needed(pools)
    create_host_if_needed()
    cleanup_env()


if __name__ == '__main__':
    local_test()
