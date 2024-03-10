from prometheus_client import Counter

from utils.cid import get_current_cid
from utils.otel import get_otel_meter

def create_counter(name, description):
    return {
        'otel': get_otel_meter().create_counter(
                    name = name,
                    description = description,
                    unit = "1"
                ),
        'prom': Counter(name, description, ['cid'])
    }

def increment_counter(counter):
    cid = get_current_cid()
    counter['otel'].add(1, {"cid": cid})
    counter['prom'].labels(cid).inc()
