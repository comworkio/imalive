import os

from datetime import datetime
from time import sleep
from metrics_utils import all_metrics

WAIT_TIME = int(os.environ['WAIT_TIME'])
NODE_NAME = os.environ['IMALIVE_NODE_NAME']

def heartbit():
    while True:
        vdate = datetime.now()
        print("[{}][{}] I'm alive! metrics = {}".format(vdate.isoformat(), NODE_NAME, all_metrics()))
        sleep(WAIT_TIME)
