import os

from datetime import datetime
from time import sleep
from metrics_utils import disk_usage

WAIT_TIME = int(os.environ['WAIT_TIME'])
NODE_NAME = os.environ['IMALIVE_NODE_NAME']

def heartbit():
    while True:
        vdate = datetime.now()
        print("[{}][{}] I'm alive! disk = {}".format(vdate.isoformat(), NODE_NAME, disk_usage()))
        sleep(WAIT_TIME)
