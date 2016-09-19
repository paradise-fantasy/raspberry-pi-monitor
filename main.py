from api import postData
from snmp_fetcher import fetchData
import time

if __name__ == "__main__":
    print "rpi-vitals-monitor started"
    while True:
	snmpData = fetchData();
	print "fetched SNMP data"
	for field, value in snmpData.iteritems():
	    print "%s: %f" % (field, value);
        postData(fetchData());
	print "posted data to API"
        time.sleep(15)
