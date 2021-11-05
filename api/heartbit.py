import os

from datetime import datetime
from time import sleep

WAIT_TIME = int(os.environ['WAIT_TIME'])
NODE_NAME = os.environ['IMALIVE_NODE_NAME']

def heartbit():
    while True:
        vdate = datetime.now()
        print("[{}][{}] I'm alive!".format(vdate.isoformat(), NODE_NAME))
        sleep(WAIT_TIME)
