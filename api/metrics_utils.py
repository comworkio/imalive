import psutil

def disk_usage():
    dd = psutil.disk_usage('/')
    div = (1024.0 ** 3)
    return {
        "status": "ok",
        "total": dd.total / div,
        "used": dd.used / div,
        "free": dd.free / div
    }
