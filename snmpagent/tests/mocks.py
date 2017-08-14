class FakeObject(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class MockUnitySystem(object):
    def __init__(self, **kwargs):
        self.model = 'Unity 500'
        self.serial_number = 'FNM00150600267'
        self.system_version = '4.2.0'

    def enable_perf_stats(self):
        pass

    def update(self):
        self.current_power = 542
        self.avg_power = 540
        self.total_iops = 0.5333333333333333
        self.read_iops = 0.13333333333333333
        self.write_iops = 0.4
        self.total_byte_rate = 2756000.2666666666664
        self.read_byte_rate = 187000.73333333333332
        self.write_byte_rate = 2568000.5333333333333

    def get_mgmt_interface(self):
        return [FakeObject(ip_address='10.10.10.10'),
                FakeObject(ip_address='10.10.10.11')]

    def get_system_capacity(self):
        return [FakeObject(size_total=3298534883328, size_used=1099511627776,
                           size_free=2199023255552),
                FakeObject(size_total=3298534883328, size_used=1099511627776,
                           size_free=2199023255552),
                FakeObject(size_total=4398046511104, size_used=1099511627776,
                           size_free=3298534883328)]

    def get_sp(self):
        return [FakeObject(name='SP A',
                           emc_serial_number='CF2HF144300003',
                           health=FakeObject(value=FakeObject(name='OK')),
                           utilization=2.628533087310241,
                           block_total_iops=0.5333333333333333,
                           block_read_iops=0.13333333333333333,
                           block_write_iops=0.4003333,
                           total_byte_rate=2756000.2666666666664,
                           read_byte_rate=187000.73333333333332,
                           write_byte_rate=2568000.5333333333333,
                           block_cache_dirty_size=65,
                           block_cache_read_hit_ratio=100.5333333333333,
                           block_cache_write_hit_ratio=81.9672131147541
                           ),
                FakeObject(name='SP B',
                           block_total_iops=0,
                           block_read_iops=0,
                           block_write_iops=0,
                           total_byte_rate=0,
                           read_byte_rate=0,
                           write_byte_rate=0,
                           block_cache_dirty_size=0,
                           block_cache_read_hit_ratio=0,
                           block_cache_write_hit_ratio=0
                           ),
                FakeObject(name='SP C',
                           health=FakeObject(value=FakeObject()),
                           utilization='na',
                           block_total_iops='na',
                           block_read_iops='na',
                           block_write_iops='na',
                           total_byte_rate='na',
                           read_byte_rate='na',
                           write_byte_rate='na',
                           block_cache_dirty_size='na',
                           block_cache_read_hit_ratio='na',
                           block_cache_write_hit_ratio='na'
                           )
                ]

    def get_pool(self):
        return [FakeObject(name='Beijing',
                           tiers=[FakeObject(name='Extreme Performance',
                                             disk_count=10),
                                  FakeObject(name='Performance',
                                             disk_count=10),
                                  FakeObject(name='Capacity', disk_count=10),
                                  ],
                           raid_type=FakeObject(name='RAID10'),
                           is_fast_cache_enabled=True,
                           size_total=3000000000000,
                           size_free=1000000000000,
                           size_used=2000000000000,
                           ),
                FakeObject(name='Shanghai',
                           size_total=0,
                           size_free=0,
                           size_used=0,
                           ),
                FakeObject(name='Shenzhen',
                           tiers=[FakeObject(name='Extreme Performance',
                                             disk_count=10),
                                  FakeObject(name='Performance',
                                             disk_count='na'),
                                  ],
                           raid_type=FakeObject(name='RAID5'),
                           is_fast_cache_enabled=False,
                           size_total='na',
                           size_free='na',
                           size_used='na',
                           )]

    def get_lun(self):
        return [FakeObject(id='sv_1',
                           name='Yangpu',
                           pool=FakeObject(raid_type=FakeObject(name='RAID10'),
                                           is_fast_cache_enabled=False),
                           size_allocated=8192,
                           size_total=107374182400,
                           health=FakeObject(value=FakeObject(name='OK')),
                           default_node=FakeObject(name='SP B'),
                           current_node=FakeObject(name='SP A'),
                           response_time=5079.653846153846,
                           queue_length=0.0103,
                           total_iops=0.43333333333333335,
                           read_iops=0.03333333333333333,
                           write_iops=0.4001,
                           total_byte_rate=2705.0666666666666,
                           read_byte_rate=136.53333333333333,
                           write_byte_rate=2568.5333333333333,
                           fast_cache_read_hits=30.0001,
                           fast_cache_write_hits=30.0001,
                           fast_cache_read_hit_rate=30.0001,
                           fast_cache_write_hit_rate=30.0301,
                           utilization=0.08120128718916914,
                           host_access=[FakeObject(host=FakeObject(
                               name='ESD-HOST193221.meng.lab.emc.com')),
                               FakeObject(host=FakeObject(
                                   name='10.245.54.151')),
                               FakeObject(host=FakeObject(
                                   name='VPI25224')), ],
                           ),
                FakeObject(id='sv_2'),
                FakeObject(id='sv_3',
                           name="Pudong",
                           pool=FakeObject(),
                           size_allocated=0,
                           size_total=0,
                           health=FakeObject(),
                           default_node=FakeObject(),
                           current_node=FakeObject(),
                           response_time=0,
                           queue_length=0,
                           total_iops=0,
                           read_iops=0,
                           write_iops=0,
                           total_byte_rate=0,
                           read_byte_rate=0,
                           write_byte_rate=0,
                           fast_cache_read_hits=0,
                           fast_cache_write_hits=0,
                           fast_cache_read_hit_rate=0,
                           fast_cache_write_hit_rate=0,
                           utilization=0,
                           host_access=[],
                           ),
                FakeObject(id='sv_4',
                           name="Jing'an",
                           pool=FakeObject(is_fast_cache_enabled=True),
                           size_allocated='nan',
                           size_total='nan',
                           health=FakeObject(value=FakeObject(name='OK BUT')),
                           default_node=FakeObject(name='SP A'),
                           current_node=FakeObject(name='SP B'),
                           response_time='nan',
                           queue_length='nan',
                           total_iops='nan',
                           read_iops='nan',
                           write_iops='nan',
                           total_byte_rate='nan',
                           read_byte_rate='nan',
                           write_byte_rate='nan',
                           fast_cache_read_hits='nan',
                           fast_cache_write_hits='nan',
                           fast_cache_read_hit_rate='nan',
                           fast_cache_write_hit_rate='nan',
                           utilization='nan',
                           host_access=[],
                           ),
                ]

    def get_disk(self):
        return [FakeObject(name='DPE Drive 0',
                           model='HU415606 EMC600',
                           emc_serial_number='0XG507BJ',
                           version='K7P0',
                           disk_technology=FakeObject(name='SAS'),
                           slot_number=0,
                           health=FakeObject(value=FakeObject(name='OK')),
                           raw_size=590894538752,
                           pool=FakeObject(name='Shanghai'),
                           response_time=35337.374655647385,
                           queue_length=1.2121212121212122,
                           total_iops=2.2,
                           read_iops=1.4166666666666667,
                           write_iops=0.7833333333333333,
                           total_byte_rate=1330312.5333333332,
                           read_byte_rate=1123601.0666666667,
                           write_byte_rate=206711.46666666667,
                           utilization=22.450302271134017,
                           ),
                FakeObject(name='DPE Drive 1'),
                FakeObject(name='DAE 0 1 Drive 0',
                           model='ST2000NK EMC2000',
                           emc_serial_number='Z4H027TW',
                           version='MN16',
                           disk_technology='NL_SAS',
                           slot_number=1,
                           health=FakeObject(),
                           raw_size=0,
                           pool=FakeObject(),
                           response_time=0,
                           queue_length=0,
                           total_iops=0,
                           read_iops=0,
                           write_iops=0,
                           total_byte_rate=0,
                           read_byte_rate=0,
                           write_byte_rate=0,
                           utilization=0,
                           ),
                FakeObject(name='DAE 0 1 Drive 1',
                           model='ST2000NK EMC2000',
                           emc_serial_number='Z4H027TW',
                           version='MN16',
                           disk_technology='NL_SAS',
                           slot_number=1,
                           health=FakeObject(value=FakeObject(name='MAJOR')),
                           raw_size='nan',
                           pool=FakeObject(name='Shanghai'),
                           response_time='nan',
                           queue_length='nan',
                           total_iops='nan',
                           read_iops='nan',
                           write_iops='nan',
                           total_byte_rate='nan',
                           read_byte_rate='nan',
                           write_byte_rate='nan',
                           utilization='nan',
                           ),
                ]

    def get_iscsi_node(self):
        return [FakeObject(id='iscsinode_spa_eth1',
                           name='iqn.1992-04.com.emc:cx.fnm00150600267.a0',
                           ethernet_port=FakeObject(
                               connector_type=FakeObject(name='RJ45'),
                               speed=FakeObject(name='_10GbPS'),
                               supported_speeds=[FakeObject(name='_1GbPS'),
                                                 FakeObject(name='_10GbPS'),
                                                 FakeObject(name='_100MbPS'),
                                                 FakeObject(name='AUTO')],
                               health=FakeObject(
                                   value=FakeObject(name='OK BUT')), ),
                           total_iops=0.5333333333333333,
                           read_iops=0.13333333333333333,
                           write_iops=0.4001,
                           total_byte_rate=2645.333333333333,
                           read_byte_rate=187.73333333333332,
                           write_byte_rate=2457.6,
                           ),
                FakeObject(id='iscsinode_spa_eth2',
                           ethernet_port=FakeObject(
                               connector_type=FakeObject(),
                               supported_speeds=[FakeObject(name='_1GbPS'),
                                                 FakeObject(),
                                                 FakeObject(name='_100MbPS'),
                                                 FakeObject(name='AUTO')],
                               health=FakeObject(value=FakeObject())),
                           total_iops='nan',
                           read_iops='nan',
                           write_iops='nan',
                           total_byte_rate='nan',
                           read_byte_rate='nan',
                           write_byte_rate='nan',
                           ),
                ]

    def get_fc_port(self):
        return [FakeObject(id='spa_fc1',
                           name='SP A FC Port 1',
                           connector_type=FakeObject(name='LC'),
                           current_speed=FakeObject(name='_8GbPS'),
                           available_speeds=[FakeObject(name='_4GbPS'),
                                             FakeObject(name='_8GbPS'),
                                             FakeObject(name='_16GbPS'),
                                             FakeObject(name='AUTO')],
                           health=FakeObject(value=FakeObject(name='MAJOR')),
                           total_iops=0,
                           read_iops=0,
                           write_iops=0,
                           total_byte_rate=0,
                           read_byte_rate=0,
                           write_byte_rate=0,
                           ),
                FakeObject(id='spb_fc2'), ]

    def get_iscsi_portal(self):
        return [FakeObject(ip_address='10.0.0.10',
                           iscsi_node=FakeObject(id='iscsinode_spa_eth1')),
                FakeObject(iscsi_node=FakeObject(id='iscsinode_spb_eth2'))]

    def get_sas_port(self):
        return [FakeObject(id='spa_sas0',
                           name='SP A SAS Port 0',
                           connector_type=FakeObject(name='MINI_SAS_HD'),
                           port=0,
                           current_speed=FakeObject(name='_12Gbps'),
                           parent_io_module=FakeObject(name='IO Module A'),
                           parent_storage_processor=FakeObject(name='SP A'),
                           health=FakeObject(value=FakeObject(name='OK')),
                           ),
                FakeObject(id='spb_sas0')]

    def get_host(self):
        return [FakeObject(name='ubuntu1604',
                           ip_list=['10.207.84.27',
                                    '2620:0:170:1d34:a236:9fff:fe66:8960',
                                    '2620:0:170:1d36:a236:9fff:fe66:8960'],
                           iscsi_host_initiators=[FakeObject(
                               initiator_id='iqn.1993-08.org.debian:01:b97\
                               4ee37fea')],
                           fc_host_initiators=[FakeObject(
                               initiator_id='20:00:00:90:FA:53:49:28:10:00\
                               :00:90:FA:53:49:28'),
                               FakeObject(
                                   initiator_id='20:00:00:90:FA:53:49:29:1\
                                   0:00:00:90:FA:53:49:29')],
                           os_type='Linux',
                           host_luns=[FakeObject(
                               lun=FakeObject(name='storops_dummy_lun'))],
                           ),
                FakeObject(name='10.245.54.151'),
                FakeObject(name='10.245.54.152',
                           ip_list=[],
                           iscsi_host_initiators=[],
                           fc_host_initiators=[FakeObject(
                               initiator_id='20:00:00:90:FA:53:49'),
                               FakeObject(
                                   initiator_id='20:00:00:90:FA:53:50')],
                           os_type='VMware ESXi 6.0.0',
                           host_luns=[],
                           ),
                FakeObject(name='10.245.54.153',
                           ip_list=[],
                           iscsi_host_initiators=[FakeObject(
                               initiator_id='iqn.1993-08.org.debian:01:b97\
                               4ee37fea')],
                           os_type='VMware ESXi 6.0.0',
                           host_luns=[],
                           ),
                FakeObject(name='10.245.54.154',
                           ip_list=[],
                           iscsi_host_initiators=[],
                           fc_host_initiators=[],
                           os_type='VMware ESXi 6.0.0',
                           host_luns=[],
                           ),
                ]

    def get_dae(self):
        return [FakeObject(name='DAE 0 1',
                           model='ANCHO LF 12G SAS DAE',
                           emc_serial_number='CF22W145100058',
                           emc_part_number='100-900-000-04',
                           health=FakeObject(value=FakeObject(name='OK')),
                           current_power=430,
                           avg_power=428,
                           max_power=458,
                           current_temperature=26,
                           avg_temperature=25,
                           max_temperature=30,
                           ),
                FakeObject(name='DAE 0 2')]

    def get_dpe(self):
        return [FakeObject(name='DPE 1',
                           model='OBERON 25 DRIVE CHASSIS',
                           emc_serial_number='CF2CV145000001',
                           emc_part_number='100-542-901-05',
                           health=FakeObject(
                               value=FakeObject(name='CRITICAL')),
                           current_power=0,
                           avg_power=0,
                           max_power=0,
                           current_temperature=0,
                           avg_temperature=0,
                           max_temperature=0, ),
                FakeObject(name='DPE 2',
                           current_power='nan',
                           avg_power='nan',
                           max_power='nan',
                           current_temperature='nan',
                           avg_temperature='nan',
                           max_temperature='nan', )]

    def get_power_supply(self):
        return [FakeObject(name='DPE Power Supply A0',
                           manufacturer='FLEXTRONICS POWER INC.',
                           model='12V P/S WITH 12VSTBY AND FAN',
                           firmware_version='0501',
                           parent_dpe=FakeObject(name='DPE'),
                           parent_dae=FakeObject(name='DAE'),
                           storage_processor=FakeObject(name='SP A'),
                           health=FakeObject(
                               value=FakeObject(name='OK')),
                           ),
                FakeObject(name='DAE 0 1 Power Supply B0')]

    def get_fan(self):
        return [FakeObject(name='DPE Cooling Module A0',
                           slot_number=0,
                           parent_dpe=FakeObject(name='DPE'),
                           parent_dae=FakeObject(name='DAE 0 1'),
                           health=FakeObject(value=FakeObject(name='OK')),
                           ),
                FakeObject(name='DPE Cooling Module A1',
                           slot_number=0,
                           parent_dpe=FakeObject(name='DPE'),
                           health=FakeObject(value=FakeObject(name='OK')),
                           ),
                FakeObject(name='DPE Cooling Module A2',
                           slot_number=0,
                           parent_dae=FakeObject(name='DAE 0 1'),
                           health=FakeObject(value=FakeObject(name='OK')),
                           ),
                FakeObject(name='DPE Cooling Module B1',
                           slot_number=None,
                           )]

    def get_battery(self):
        return [FakeObject(name='SP A Battery 0',
                           manufacturer='ACBEL POLYTECH INC.',
                           model='LITHIUM-ION, UNIVERSAL BOB',
                           firmware_version='073.91',
                           parent_storage_processor=FakeObject(name='SP A'),
                           health=FakeObject(value=FakeObject(name='OK')), ),
                FakeObject(name='SP B Battery 0')]
