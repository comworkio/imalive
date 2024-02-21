import os
import psutil

from datetime import datetime
from psutil._common import bytes2human

from utils.logger import log_msg

def disk_usage():
    dd = psutil.disk_usage('/')
    div = (1024.0 ** 3)
    total_gb = dd.total / div
    used_gb = dd.used / div
    free_gb = dd.free / div
    percent_used = (used_gb / total_gb) * 100

    return {
        "total": total_gb,
        "used": used_gb,
        "free": free_gb,
        "percent": percent_used
    }

def virtual_memory():
    mem = psutil.virtual_memory()
    total = bytes2human(mem.total)
    available = bytes2human(mem.available)
    used = bytes2human(mem.used)
    percent_used = (mem.used / mem.total) * 100
    return {
        "total": total,
        "used": used,
        "available": available,
        "percent": percent_used,
    }

def swap_memory():
    sw = psutil.swap_memory()
    return {
        "total": bytes2human(sw.total),
        "used": bytes2human(sw.used),
        "free": bytes2human(sw.free),
        "percent": sw.percent
    }

def cpu():
    return {
        "percent": {
            "all": psutil.cpu_percent(interval=1),
            "percpu": psutil.cpu_percent(interval=1, percpu=True)
        },
        "count": {
            "all": psutil.cpu_count(),
            "with_logical": psutil.cpu_count(logical=False)
        },
        "times": {
            "all": psutil.cpu_times(),
            "percpu": psutil.cpu_times(percpu=True)
        }
    }

def all_metrics():
    vdate = datetime.now()
    return {
        "status": "ok",
        'name': os.environ['IMALIVE_NODE_NAME'],
        'time': vdate.isoformat(),
        "disk_usage": disk_usage(),
        "virtual_memory": virtual_memory(),
        "swap_memory": swap_memory(),
        "cpu": cpu()
    }

def log_usage_if_needed(level, current_value, threshold, type):
    if current_value > threshold:
        log_msg(level, f"[metrics] {type} usage is above {threshold}%: {current_value}%")
        return True
    return False

def check_and_log_usage(metric_type, metric_value, warning_threshold, error_threshold):
    if not log_usage_if_needed("ERROR", metric_value, error_threshold, metric_type):
        log_usage_if_needed("WARN", metric_value, warning_threshold, metric_type)
