import logging
import random
import time
import unittest

from snmpagent_unity.comptests import cli_helper
from snmpagent_unity.comptests import perf
from snmpagent_unity.comptests import snmpclient
from snmpagent_unity.comptests import utils as comp_utils

LOG = logging.getLogger(__name__)


class TestTableViewPerf(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create pool, lun and host if need
        pools = comp_utils.create_pool_if_needed()
        comp_utils.create_lun_if_needed(pools)
        comp_utils.create_host_if_needed()

        # Cleanup env
        cls.helper = cli_helper.Helper()
        cls.helper.stop_service()
        cls.helper.clear_access_data()

        # Get config
        config = comp_utils.get_env_yaml()
        for command in config['snmp_commands']:
            if command.get('name'):
                cls.snmptable_path = command.get('path')
                break

        cls.agent_ip = config.get('agent').get('ip')
        cls.agent_port = random.choice(config.get('agent').get('ports'))
        LOG.info('SNMP Agent port to be tested: {}'.format(cls.agent_port))

        community = config.get('v2_user')[0].get('name')

        # Create snmp client
        cls._snmp_client = snmpclient.SNMPv2Client(cls.agent_ip,
                                                   cls.agent_port, community)

        # Add community in agent
        cls.helper.create_community(community)

        # Start agent
        cls.helper.start_service()

        # Wait 300 sec to make sure agent service and metrics ready
        time.sleep(300)

    @classmethod
    def tearDownClass(cls):
        comp_utils.cleanup_env()
        cls.helper.stop_service()
        cls.helper.clear_access_data()

    def test_all_tables(self):
        tables = ['bbuTable', 'fanTable', 'powerSupplyTable', 'enclosureTable',
                  'hostTable', 'backendPortTable', 'frontendPortTable',
                  'diskTable', 'volumeTable', 'poolTable',
                  'storageProcessorTable']

        times = 10
        prefix = 'perf_test_result'
        ts = perf.get_time_stamp()

        perf_rst = perf.run_perf(tables, self.agent_ip, self.agent_port, times,
                                 cmd_path=self.snmptable_path)

        perf.save_to_json(
            '{}_{}_{}.json'.format(prefix, ts, str(self.agent_port)), perf_rst)
        perf.save_to_csv(
            '{}_{}_{}.csv'.format(prefix, ts, str(self.agent_port)), perf_rst)
