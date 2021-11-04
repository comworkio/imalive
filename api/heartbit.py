import os

from time import sleep

WAIT_TIME = os.environ['WAIT_TIME']
NODE_NAME = os.environ['IMALIVE_NODE_NAME']

def heartbit():
    while True:
        print("I'm alive! {}".format(NODE_NAME))
        sleep(WAIT_TIME)
