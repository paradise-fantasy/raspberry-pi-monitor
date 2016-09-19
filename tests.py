from output_processing import parseLoad, parseTemp, parseMemTotal, parseMemAvail, parseDiskTotal, parseDiskAvail

assert parseLoad(
    'UCD-SNMP-MIB::laLoad.1 = STRING: 0.71\nUCD-SNMP-MIB::laLoad.2 = STRING: 0.29\nUCD-SNMP-MIB::laLoad.3 = STRING: 0.16',0
    ) == 0.71;
assert parseTemp("temp=48.7'C") == 48.7;

assert parseMemTotal('UCD-SNMP-MIB::memTotalReal.0 = INTEGER: 445112 kB') == 445112;
assert parseMemAvail('UCD-SNMP-MIB::memAvailReal.0 = INTEGER: 165444 kB') == 165444;
assert parseDiskTotal('UCD-SNMP-MIB::dskTotal.1 = INTEGER: 15107224') == 15107224;
assert parseDiskAvail('UCD-SNMP-MIB::dskUsed.1 = INTEGER: 1649508') == 1649508;



# UCD-SNMP-MIB::laLoad.2 = STRING: 0.29

# UCD-SNMP-MIB::laLoad.3 = STRING: 0.16

# temp=48.7'C

# UCD-SNMP-MIB::memTotalReal.0 = INTEGER: 445112 kB

# UCD-SNMP-MIB::memAvailReal.0 = INTEGER: 165444 kB

# UCD-SNMP-MIB::dskTotal.1 = INTEGER: 15107224

#UCD-SNMP-MIB::dskUsed.1 = INTEGER: 1649508
