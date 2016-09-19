from api import postData
from snmp_fetcher import fetchData
import time

if __name__ == "__main__":
    while True:
        postData(fetchData());
        time.sleep(15)
