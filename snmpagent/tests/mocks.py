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
        self.total_byte_rate = 2747.733333333333
        self.read_byte_rate = 187.73333333333332
        self.write_byte_rate = 2560.0

    def get_mgmt_interface(self):
        return [FakeObject(ip_address='10.10.10.10'),
                FakeObject(ip_address='10.10.10.11')]

    def get_system_capacity(self):
        return [FakeObject(size_total=3000000000000, size_used=1000000000000,
                           size_free=2000000000000),
                FakeObject(size_total=3000000000000, size_used=1000000000000,
                           size_free=2000000000000),
                FakeObject(size_total=4000000000000, size_used=1000000000000,
                           size_free=3000000000000)]

    def get_sp(self):
        return [FakeObject(name='SP A', emc_serial_number='CF2HF144300003',
                           health=FakeObject(value=FakeObject(name='OK')),
                           utilization=2.628533087310241,
                           block_total_iops=0.5333333333333333,
                           block_read_iops=0.13333333333333333,
                           block_write_iops=0.4003333,
                           total_byte_rate=2756.2666666666664,
                           read_byte_rate=187.73333333333332,
                           write_byte_rate=2568.5333333333333,
                           block_cache_dirty_size=65,
                           block_cache_read_hit_ratio=100.5333333333333,
                           block_cache_write_hit_ratio=81.9672131147541
                           ),
                FakeObject(name='SP B', emc_serial_number='CF2HF144600021',
                           health=FakeObject(value=FakeObject(name='OK')),
                           utilization=29.030090220258398,
                           block_total_iops=0,
                           block_read_iops=0,
                           block_write_iops=0,
                           total_byte_rate=0,
                           read_byte_rate=0,
                           write_byte_rate=0,
                           block_cache_dirty_size=92,
                           block_cache_read_hit_ratio=100.0,
                           block_cache_write_hit_ratio=38.02597402597402
                           )]

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
                           tiers=[FakeObject(name='Extreme Performance',
                                             disk_count=10),
                                  FakeObject(name='Performance',
                                             disk_count=10),
                                  ],
                           raid_type=FakeObject(name='RAID5'),
                           is_fast_cache_enabled=False,
                           size_total=3000000000000,
                           size_free=2000000000000,
                           size_used=1000000000000,
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
                           fast_cache_write_hit_rate=30.0001,
                           utilization=0.08120128718916914,
                           host_access=[FakeObject(host=FakeObject(
                               name='ESD-HOST193221.meng.lab.emc.com')),
                               FakeObject(host=FakeObject(
                                   name='10.245.54.151')),
                               FakeObject(host=FakeObject(
                                   name='VPI25224')), ],
                           ),
                FakeObject(id='sv_2',
                           name="Jing'an",
                           pool=FakeObject(is_fast_cache_enabled=True),
                           size_allocated=0,
                           size_total=0,
                           health=FakeObject(value=FakeObject(name='OK BUT')),
                           default_node=FakeObject(name='SP A'),
                           current_node=FakeObject(name='SP B'),
                           response_time=0,
                           queue_length=0,
                           total_iops=0,
                           read_iops=0,
                           write_iops=0,
                           total_byte_rate=0,
                           read_byte_rate=0,
                           write_byte_rate=0,
                           fast_cache_read_hits='nan',
                           fast_cache_write_hits='nan',
                           fast_cache_read_hit_rate='nan',
                           fast_cache_write_hit_rate='nan',
                           utilization=0,
                           host_access=[],
                           )]

    def get_disk(self):
        return [FakeObject(name='DPE Drive 0',
                           model='HU415606 EMC600',
                           emc_serial_number='0XG507BJ',
                           version='K7P0',
                           disk_technology=FakeObject(name='SAS'),
                           slot_number=0,
                           health=FakeObject(value=FakeObject(name='OK')),
                           raw_size=590894538752,
                           # pool=,
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
                FakeObject(name='DAE 0 1 Drive 0',
                           model='ST2000NK EMC2000',
                           emc_serial_number='Z4H027TW',
                           version='MN16',
                           disk_technology='NL_SAS',
                           slot_number=1,
                           health=FakeObject(value=FakeObject(name='MAJOR')),
                           raw_size=0,
                           pool=FakeObject(name='Shanghai'),
                           response_time=0,
                           queue_length=0,
                           total_iops=0,
                           read_iops=0,
                           write_iops=0,
                           total_byte_rate=0,
                           read_byte_rate=0,
                           write_byte_rate=0,
                           utilization=0,
                           ), ]

    def get_fc_port(self):
        return [FakeObject(id='spa_fc4',
                           name='SP A FC Port 4',
                           connector_type=FakeObject(name='LC'),
                           current_speed=FakeObject(name='_8GbPS'),
                           available_speeds=[FakeObject(name='_4GbPS'),
                                             FakeObject(name='_8GbPS'),
                                             FakeObject(name='_16GbPS'),
                                             FakeObject(name='AUTO')],
                           health=FakeObject(value=FakeObject(name='OK')),
                           total_iops=0,
                           read_iops=0,
                           write_iops=0,
                           total_byte_rate=0,
                           read_byte_rate=0,
                           write_byte_rate=0,
                           ),
                FakeObject(id='spb_fc4')]

    def get_iscsi_node(self):
        return [FakeObject(id='iscsinode_spa_eth2',
                           name='iqn.1992-04.com.emc:cx.fnm00150600267.a0',
                           ethernet_port=FakeObject(
                               connector_type=FakeObject(name='RJ45'),
                               speed=FakeObject(name='_10GbPS'),
                               supported_speeds=[FakeObject(name='_1GbPS'),
                                                 FakeObject(name='_10GbPS'),
                                                 FakeObject(name='_100GbPS'),
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
                FakeObject(id='iscsinode_spb_eth2')]

    def get_iscsi_portal(self):
        return [FakeObject(ip_address='10.0.0.10',
                           iscsi_node=FakeObject(id='iscsinode_spa_eth2')),
                FakeObject(iscsi_node=FakeObject(id='iscsinode_spa_eth2'))]

    def get_sas_port(self):
        return [FakeObject(id='spa_sas0'),
                FakeObject(id='spb_sas0')]

    def get_host(self):
        pass

    def get_dae(self):
        return [FakeObject(name='DAE 0 1'),
                FakeObject(name='DAE 0 2')]

    def get_dpe(self):
        return [FakeObject(name='DPE 1'),
                FakeObject(name='DPE 2')]

    def get_power_supply(self):
        return [FakeObject(name='DPE Power Supply A0'),
                FakeObject(name='DPE Power Supply B0'),
                FakeObject(name='DAE 0 1 Power Supply A0'),
                FakeObject(name='DAE 0 1 Power Supply B0')]

    def get_fan(self):
        return [FakeObject(name='DPE Cooling Module A0'),
                FakeObject(name='DPE Cooling Module A1'),
                FakeObject(name='DPE Cooling Module A2'),
                FakeObject(name='DPE Cooling Module A3'),
                FakeObject(name='DPE Cooling Module A4'),
                FakeObject(name='DPE Cooling Module B1'),
                FakeObject(name='DPE Cooling Module B2'),
                FakeObject(name='DPE Cooling Module B3'),
                FakeObject(name='DPE Cooling Module B4'),
                FakeObject(name='DPE Cooling Module B5')]

    def get_bbu(self):
        pass
