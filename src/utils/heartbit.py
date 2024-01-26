import os

from datetime import datetime
from time import sleep
from utils.metrics import all_metrics
from utils.common import is_enabled
from utils.logger import log_msg

WAIT_TIME = int(os.environ['WAIT_TIME'])
NODE_NAME = os.environ['IMALIVE_NODE_NAME']
LOG_FORMAT = os.environ['LOG_FORMAT']

def heartbit():
    while True:
        vdate = datetime.now()
        if is_enabled(LOG_FORMAT):
            log_msg("INFO", "[metrics] I'm alive! metrics = {}".format(all_metrics()))
        else:
            print("[{}][{}] I'm alive! metrics = {}".format(vdate.isoformat(), NODE_NAME, all_metrics()))
        sleep(WAIT_TIME)
