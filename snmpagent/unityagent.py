from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.proto.api import v2c
from pysnmp.smi import builder
from pysnmp import debug

debug.setLogger(debug.Debug('all'))

# Create SNMP engine
snmpEngine = engine.SnmpEngine()

# Transport setup

# UDP over IPv4
config.addTransport(
    snmpEngine,
    udp.domainName,
    udp.UdpTransport().openServerMode(('0.0.0.0', 161))
)

# SNMPv3/USM setup

# user: usr-md5-des, auth: MD5, priv DES
# snmpwalk -v3 -u usr-md5-des -l authPriv -A authkey1 -X privkey1 localhost .1.3.6
# snmpget -v3 -u usr-md5-des -l authPriv -A authkey1 -X privkey1 localhost .1.3.6.1.4.1.1139.103.2.1.0
config.addV3User(
    snmpEngine, 'usr-md5-des',
    config.usmHMACMD5AuthProtocol, 'authkey1',
    # config.usmDESPrivProtocol, 'privkey1'
    config.usm3DESEDEPrivProtocol, 'privkey1'
)

# Allow read MIB access for this user / securityModels at VACM
config.addVacmUser(snmpEngine, 3, 'usr-md5-des', 'authPriv', (1, 3, 6, 1, 4, 1, 1139, 103, 2))

# Create an SNMP context
snmpContext = context.SnmpContext(snmpEngine)

# --- create custom Managed Object Instance ---

mibBuilder = snmpContext.getMibInstrum().getMibBuilder()
mibSources = mibBuilder.getMibSources() + (builder.DirMibSource('./mibs/'),)
mibBuilder.setMibSources(*mibSources)

MibScalar, MibScalarInstance = mibBuilder.importSymbols(
    'SNMPv2-SMI', 'MibScalar', 'MibScalarInstance'
)

(unityStorageObjects,
 agentVersion,
 mibVersion) = mibBuilder.importSymbols(
    'Unity-MIB',
    'unityStorageObjects',
    'agentVersion',
    'mibVersion'
)


class AgentVersionScalarInstance(MibScalarInstance):
    def getValue(self, name, idx):
        return self.getSyntax().clone(
            'Agent Version: v2.0'
        )


class MibVersionScalarInstance(MibScalarInstance):
    def getValue(self, name, idx):
        return self.getSyntax().clone(
            'Mib Version: v3.0'
        )


mibBuilder.exportSymbols(
    '__Unity_MIB', MibScalar(unityStorageObjects.name, v2c.OctetString()),
    AgentVersionScalarInstance(agentVersion.name, (0,), v2c.OctetString()),
    MibVersionScalarInstance(mibVersion.name, (0,), v2c.OctetString())
)

# --- end of Managed Object Instance initialization ----

# Register SNMP Applications at the SNMP engine for particular SNMP context
cmdrsp.GetCommandResponder(snmpEngine, snmpContext)
cmdrsp.NextCommandResponder(snmpEngine, snmpContext)
cmdrsp.BulkCommandResponder(snmpEngine, snmpContext)

# Register an imaginary never-ending job to keep I/O dispatcher running forever
snmpEngine.transportDispatcher.jobStarted(1)

# Run I/O dispatcher which would receive queries and send responses
try:
    snmpEngine.transportDispatcher.runDispatcher()
except:
    snmpEngine.transportDispatcher.closeDispatcher()
    raise
