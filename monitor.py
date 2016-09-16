#!/usr/bin/python
# -*- coding: utf-8 -*-
debug = 1


import subprocess

load = "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::laLoad"
temperature = "/opt/vc/bin/vcgencmd measure_temp"
mem_total_real = "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::memTotalReal.0"
mem_avail_real = "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::memAvailReal.0"
disk_total = "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::dskTotal.1"
disk_avail = "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::dskUsed.1"


get_load_ubuntu = "snmpwalk -c public -v 2c localhost:161 .1.3.6.1"

def command(command):
    temp = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)
    output = temp.communicate()[0]
    return output




def main():
    if debug:
        print(command(get_load_ubuntu))
    else:
        print command(get_load)
        print command(get_temp)

if __name__ == "__main__":
    main()
