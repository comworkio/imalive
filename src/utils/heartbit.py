import os

from datetime import datetime
from time import sleep
from utils.metrics import all_metrics
from utils.common import is_true

WAIT_TIME = int(os.environ['WAIT_TIME'])
NODE_NAME = os.environ['IMALIVE_NODE_NAME']
HEART_BIT_LOG_JSON = os.environ['HEART_BIT_LOG_JSON']

def heartbit():
    while True:
        vdate = datetime.now()
        if is_true(HEART_BIT_LOG_JSON):
            print(all_metrics())
        else:
            print("[{}][{}] I'm alive! metrics = {}".format(vdate.isoformat(), NODE_NAME, all_metrics()))
        sleep(WAIT_TIME)
