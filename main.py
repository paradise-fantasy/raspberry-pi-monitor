from api import postData
from snmp_fetcher import fetchData
import time
import logging

logging.basicConfig(filename="logs/output.log", level=logging.DEBUG)

if __name__ == "__main__":
    print "[*] Raspberry-vitals-monitor started"
    while True:
	snmpData = fetchData();
	print "[*] Fetched SNMP data"
	for field, value in snmpData.iteritems():
	    print "[*] %s: %f" % (field, value);
        postData(snmpData);
	print "[*] Posted data to API"
        time.sleep(15)
