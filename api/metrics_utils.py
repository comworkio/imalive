import psutil

from psutil._common import bytes2human

def disk_usage():
    dd = psutil.disk_usage('/')
    div = (1024.0 ** 3)
    return {
        "total": dd.total / div,
        "used": dd.used / div,
        "free": dd.free / div
    }

def virtual_memory():
    mem = psutil.virtual_memory()
    return {
        "total": bytes2human(mem.total),
        "available": bytes2human(mem.available)
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
    return {
        "status": "ok",
        "disk_usage": disk_usage(),
        "virtual_memory": virtual_memory(),
        "swap_memory": swap_memory(),
        "cpu": cpu()
    }