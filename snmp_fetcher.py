import subprocess
from output_processing import parseLoad, parseTemp, parseMemTotal, parseMemAvail, parseDiskTotal, parseDiskAvail

load_avg_interval = 0; # Set to 0 for 1min avg, 1 for 5min avg and 2 for 15min avg
debug = 0;

## The SNMP-MIB can be found at
## http://www.net-snmp.org/docs/mibs/UCD-SNMP-MIB.txt
SNMP = {
    'load': "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::laLoad",
    'temperature': "/opt/vc/bin/vcgencmd measure_temp",
    'mem_total': "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::memTotalReal.0",
    'mem_avail': "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::memAvailReal.0",
    'disk_total': "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::dskTotal.1",
    'disk_avail': "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::dskUsed.1",
    'ubuntu': "snmpwalk -c public -v 2c localhost:161 .1.3.6.1"
}


def command(command):
 temp = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)
 output = temp.communicate()[0]
 return output

def fetchData():
    if debug:
        data = { 'ubuntu': command(SNMP['ubuntu']) }
    else:
        data = {
            'load': parseLoad(command(SNMP['load']), load_avg_interval),
            'temperature': parseTemp(command(SNMP['temperature'])),
            'mem_total': parseMemTotal(command(SNMP['mem_total'])),
            'mem_avail': parseMemAvail(command(SNMP['mem_avail'])),
            'disk_total': parseDiskTotal(command(SNMP['disk_total'])),
            'disk_avail': parseDiskAvail(command(SNMP['disk_avail']))
        };
    return data;
