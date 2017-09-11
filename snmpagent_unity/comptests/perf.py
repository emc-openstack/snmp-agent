import collections
import csv
import json
import logging
import subprocess
import time
from datetime import datetime

LOG = logging.getLogger(__name__)


def snmptable_command(cmd_path, table, ip, port, version=2, community='public',
                      timeout=60, mib_name='Unity-MIB'):
    lst = [cmd_path]
    if version == 2:
        lst.extend(['-v2c', '-c', community])

    if version == 3:
        # TODO: to be implemented
        return False

    lst.extend(['-t', str(timeout), '-Os', '-Ci', ':'.join((ip, str(port))),
                '::'.join((mib_name, table))])

    return ' '.join(lst)


def get_time_stamp():
    return datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")


def save_to_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)


def save_to_csv(file_name, data, float_length=3):
    with open(file_name, 'w') as output:
        writer = csv.writer(output)

        keys = [str(x) for x in
                sorted(int(y) for y in list(data.items())[0][1].keys())]
        heads = ['Table name', 'Average time used (sec)'] + keys
        writer.writerow(heads)

        for table, results in data.items():
            rows = [round(results.get(key).get('time'), float_length) for key
                    in keys]
            avg = round(sum(float(x) for x in rows) / len(keys), float_length)
            rows = [table, avg] + rows

            writer.writerow(rows)


def run_perf(tables, agent_ip, agent_port, times=1, detail=False,
             cmd_path='snmptable', interval=0):
    perf_rst = collections.OrderedDict()

    for i in range(1, times + 1):
        for table in tables:
            command = snmptable_command(cmd_path, table, agent_ip, agent_port)
            start_time = time.time()
            p = subprocess.Popen(command, shell=True, stdin=None,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            out, err = p.communicate()
            time_used = time.time() - start_time

            rc = p.returncode
            LOG.debug('{}, time used: {}'.format(table, time_used))
            LOG.debug(out)

            if perf_rst.get(table) is None:
                perf_rst[table] = collections.OrderedDict()

            if perf_rst.get(table).get(str(i)) is None:
                perf_rst[table][str(i)] = collections.OrderedDict()

            perf_rst[table][str(i)]['time'] = time_used
            perf_rst[table][str(i)]['return code'] = rc

            if detail:
                perf_rst[table][str(i)]['output'] = out

            if interval > 0:
                time.sleep(interval)

    return perf_rst


if __name__ == '__main__':
    tables = ['bbuTable', 'fanTable', 'powerSupplyTable', 'enclosureTable',
              'hostTable', 'backendPortTable', 'frontendPortTable',
              'diskTable', 'volumeTable', 'poolTable',
              'storageProcessorTable']

    cmd_path = r'c:\usr\bin\snmptable.exe'
    agent_ip = '192.168.56.1'
    agent_port = 11161
    times = 10
    prefix = 'perf_test_result'

    perf_rst = run_perf(tables, agent_ip, agent_port, times,
                        cmd_path=cmd_path)

    # Save test results
    ts = get_time_stamp()
    save_to_json('{}_{}_{}.json'.format(prefix, ts, str(agent_port)),
                 perf_rst)
    save_to_csv('{}_{}_{}.csv'.format(prefix, ts, str(agent_port)),
                perf_rst)
