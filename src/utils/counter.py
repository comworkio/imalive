from prometheus_client import Counter

from utils.otel import get_otel_meter

def create_counter(name, description):
    return {
        'otel': get_otel_meter().create_counter(
                    name = name,
                    description = description,
                    unit = "1"
                ),
        'prom': Counter(name, description)
    }

def increment_counter(counter, tid):
    counter['otel'].add(1, {"tid": tid})
    counter['prom'].inc()
