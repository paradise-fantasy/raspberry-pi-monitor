def parseLoad(loadString, average):
    #Average should be 0 for 1 min average, 1 for 5 min and 2 for 15 min.

    #'UCD-SNMP-MIB::laLoad.1 = STRING: 0.71\nUCD-SNMP-MIB::laLoad.2 = STRING: 0.29\nUCD-SNMP-MIB::laLoad.3 = STRING: 0.16'
    loads = loadString.split('\n');
    load1 = loads[average];
    loadAsString = float(load1.split('UCD-SNMP-MIB::laLoad.1 = STRING:')[1])
    return loadAsString


def parseTemp(tempString):
    # temp=48.7'C
    return float(tempString[5:9])

def parseMemOrDisk(memOrDiskString, splitPrefix):
    #UCD-SNMP-MIB::memTotalReal.0 = INTEGER: 445112 kB
    memTotal = memOrDiskString.split(splitPrefix)[1];
    return int(memTotal.split(' ')[0]);

def parseMemTotal(memString):
    return parseMemOrDisk(memString, 'UCD-SNMP-MIB::memTotalReal.0 = INTEGER: ');

def parseMemAvail(memString):
    return parseMemOrDisk(memString, 'UCD-SNMP-MIB::memAvailReal.0 = INTEGER: ');

def parseDiskTotal(diskString):
    return parseMemOrDisk(diskString, 'UCD-SNMP-MIB::dskTotal.1 = INTEGER: ');

def parseDiskAvail(diskString):
    return parseMemOrDisk(diskString, 'UCD-SNMP-MIB::dskAvail.1 = INTEGER: ');
