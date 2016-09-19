import requests
import urllib
import urllib2
import json


url_post_rpi_vitals = "http://paradise-backend.herokuapp.com/api/rpi-vitals-events"

def postData(snmpData):
    jsonData = json.dumps(snmpData);
    r = requests.post(url_post_rpi_vitals, data=jsonData)
    return members
