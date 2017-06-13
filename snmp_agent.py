from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.proto.api import v2c
from pysnmp.smi import builder
from pysnmp import debug

import agent
import factory

debug.setLogger(debug.Debug('all'))


class SNMPAgent(object):
    def __init__(self):
        # To create multiple SNMPEngine
        pass
