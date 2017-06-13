#
# PySNMP MIB module Unity-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/local/share/mibs/Unity-MIB.txt
# Produced by pysmi-0.1.3 at Mon Jun  5 14:23:28 2017
# On host hyhit-VirtualBox platform Linux version 4.8.0-36-generic by user hyhit
# Using Python version 2.7.12 (default, Nov 19 2016, 06:48:10)
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1",
                                                                  "Integer",
                                                                  "ObjectIdentifier",
                                                                  "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols(
    "ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint",
    "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF",
                                                               "NotificationGroup",
                                                               "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols(
    "SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow",
    "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress",
    "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity",
    "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC",
                                                            "DisplayString",
                                                            "TextualConvention")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
emc = MibIdentifier((1, 3, 6, 1, 4, 1, 1139))
unity = MibIdentifier((1, 3, 6, 1, 4, 1, 1139, 103))
unityStorageObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1139, 103, 2))
agentVersion = MibScalar((1, 3, 6, 1, 4, 1, 1139, 103, 2, 1),
                         DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentVersion.setStatus('mandatory')
mibVersion = MibScalar((1, 3, 6, 1, 4, 1, 1139, 103, 2, 2),
                       DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mibVersion.setStatus('mandatory')
mibBuilder.exportSymbols("Unity-MIB", dod=dod, enterprises=enterprises,
                         agentVersion=agentVersion, internet=internet, org=org,
                         mibVersion=mibVersion, unity=unity, emc=emc,
                         private=private,
                         unityStorageObjects=unityStorageObjects)
