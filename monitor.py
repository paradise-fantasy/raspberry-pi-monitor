#!/usr/bin/python
# -*- coding: utf-8 -*-
debug = 0


import subprocess
import time
import request
import json


## The SNMP-MIB can be found at
## http://www.net-snmp.org/docs/mibs/UCD-SNMP-MIB.txt
load = "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::laLoad"
temperature = "/opt/vc/bin/vcgencmd measure_temp"
mem_total_real = "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::memTotalReal.0"
mem_avail_real = "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::memAvailReal.0"
disk_total = "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::dskTotal.1"
disk_avail = "snmpwalk -c public -v 2c localhost:161 UCD-SNMP-MIB::dskUsed.1"

checks = [load, temperature, mem_total_real, mem_avail_real, disk_total, disk_avail]


load_ubuntu = "snmpwalk -c public -v 2c localhost:161 .1.3.6.1"

def command(command):
    temp = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)
    output = temp.communicate()[0]
    return output

def post_presence(vitals):
    eventtype = "PERSON_ENTERED" if person.isPresent() else "PERSON_LEFT";
    r = requests.post(url_post_presence, data={"type": eventtype, "subject":person.name})
    # Should add some check if r.status_code is 200 and so on.

def getLoad():

def getTemp():
    tempInString = temp[5:9]

def get_vitals():
    load = getLoad();


def main():
    if debug:
        print(command(load_ubuntu))
    else:
        while True:

            for check in checks:
                print command(check)

            vitals = get_vitals()
            time.sleep(60)

if __name__ == "__main__":
    main()
