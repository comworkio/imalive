import os
import yaml
import requests
import asyncio
import threading

import requests
import yaml

from datetime import datetime
from time import sleep
from requests.auth import HTTPBasicAuth

from utils.common import is_empty_key, get_or_else, is_not_empty, remove_key_safely
from utils.gauge import create_gauge, set_gauge
from utils.heartbit import WAIT_TIME
from utils.logger import log_msg
from utils.otel import get_otel_tracer

def check_http_monitor(monitor, gauges):
    vdate = datetime.now()

    if monitor['type'] != 'http':
        log_msg("DEBUG", { 
            "status": "ok",
            "type": "monitor",
            "time": vdate.isoformat(),
            "message": "Not an http monitor",
            "monitor": monitor 
        })
        set_gauge(gauges['result'], 0)
        return

    if is_empty_key(monitor, 'url'):
        log_msg("ERROR", { 
            "status": "ko",
            "type": "monitor",
            "time": vdate.isoformat(),
            "message": "Missing mandatory url",
            "monitor": monitor 
        })
        set_gauge(gauges['result'], 0)
        return

    method = get_or_else(monitor, 'method', 'GET')
    timeout = get_or_else(monitor, 'timeout', 30)
    expected_http_code = get_or_else(monitor, 'expected_http_code', 200)
    expected_contain = get_or_else(monitor, 'expected_contain', None)
    username = get_or_else(monitor, 'username', None)
    password = get_or_else(monitor, 'password', None)

    auth = None
    duration = None
    if is_not_empty(username) and is_not_empty(password):
        auth = HTTPBasicAuth(username, password)

    remove_key_safely(monitor, 'username')
    remove_key_safely(monitor, 'password')

    try:
        if method == "GET":
            response = requests.get(monitor['url'], timeout=timeout, auth=auth)
            duration = response.elapsed.total_seconds()
            set_gauge(gauges['duration'], duration)
        elif method == "POST":
            response = requests.post(monitor['url'], timeout=timeout, auth=auth)
            duration = response.elapsed.total_seconds()
            set_gauge(gauges['duration'], duration)
        else:
            log_msg("ERROR", { 
                "status": "ko",
                "type": "monitor",
                "time": vdate.isoformat(),
                "message": "Not supported http method: actual = {}".format(method),
                "monitor": monitor
            })
            set_gauge(gauges['result'], 0)
            return

        if response.status_code != expected_http_code:
            log_msg("ERROR", { 
                "status": "ko",
                "type": "monitor",
                "time": vdate.isoformat(),
                "duration": duration,
                "message": "Not expected status code: expected = {}, actual = {}".format(expected_http_code, response.status_code),
                "monitor": monitor
            })
            set_gauge(gauges['result'], 0)
            return

        if is_not_empty(expected_contain) and expected_contain not in response.text:
            log_msg("ERROR", { 
                "status": "ko",
                "type": "monitor",
                "time": vdate.isoformat(),
                "duration": duration,
                "message": "Response not valid: expected = {}, actual = {}".format(expected_contain, response.text),
                "monitor": monitor
            })
            set_gauge(gauges['result'], 0)
            return

        set_gauge(gauges['result'], 1)
        log_msg("INFO", { 
            "status": "ok",
            "type": "monitor",
            "time": vdate.isoformat(),
            "duration": duration,
            "message": "Monitor is healthy",
            "monitor": monitor
        })

    except Exception as e:
        set_gauge(gauges['result'], 0)
        log_msg("ERROR", {
            "status": "ko",
            "type": "monitor",
            "time": vdate.isoformat(),
            "message": "Unexpected error",
            "error": "{}".format(e),
            "monitor": monitor
        })

gauges = {}
def monitors():
    def loop_monitors():
        config_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'imalive.yml'))
        with open(config_path, "r") as stream:
            loaded_data = yaml.safe_load(stream)
            for monitor in loaded_data['monitors']:
                if is_empty_key(monitor, 'name'):
                    continue

                gauges[monitor['name']] = {
                    'result': create_gauge("monitor_{}_result".format(monitor['name']), "monitor {} result".format(monitor['name'])),
                    'duration': create_gauge("monitor_{}_duration".format(monitor['name']), "monitor {} duration".format(monitor['name']))
                }

            while True:
                with get_otel_tracer().start_as_current_span("imalive-monitors"):
                    for monitor in loaded_data['monitors']:
                        if is_empty_key(monitor, 'name'):
                            continue
                        check_http_monitor(monitor, gauges[monitor['name']])
                sleep(WAIT_TIME)

    def start_monitors():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(loop_monitors())

    async_thread = threading.Thread(target=start_monitors, daemon=True)
    async_thread.start()
