import os
import asyncio
import threading

from time import sleep

from utils.prom import create_gauge, set_gauge
from utils.metrics import all_metrics
from utils.logger import log_msg

WAIT_TIME = int(os.environ['WAIT_TIME'])
NODE_NAME = os.environ['IMALIVE_NODE_NAME']

cpu_gauge = create_gauge("cpu_all", "cpu usage in percent")
ram_total_gauge = create_gauge("ram_total", "total of ram")
ram_available_gauge = create_gauge("ram_available", "available ram")
disk_free_gauge = create_gauge("disk_free", "free storage's space")
disk_used_gauge = create_gauge("disk_used", "used storage's space")
disk_total_gauge = create_gauge("disk_total", "total storage's space")

def heartbit():
    def loop_heartbit():
        while True:
            metrics = all_metrics()
            log_msg("INFO", "[metrics] I'm alive! metrics = {}".format(metrics))
            set_gauge(cpu_gauge, metrics['cpu']['percent']['all'])
            set_gauge(ram_total_gauge, metrics['virtual_memory']['total'])
            set_gauge(ram_available_gauge, metrics['virtual_memory']['available'])
            set_gauge(disk_free_gauge, metrics['disk_usage']['free'])
            set_gauge(disk_used_gauge, metrics['disk_usage']["used"])
            set_gauge(disk_total_gauge, metrics['disk_usage']["total"])
            sleep(WAIT_TIME)

    def start_heartbit():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(loop_heartbit())

    async_thread = threading.Thread(target=start_heartbit, daemon=True)
    async_thread.start()
