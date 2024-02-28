import re

from prometheus_client import Gauge
from opentelemetry.metrics import Observation

from utils.otel import get_otel_meter

_numeric_value_pattern = r"-?\d+\.\d+"
_current_gauge_values = {}

def create_gauge(name, description):
    _current_gauge_values[name] = {
        'val': 0.0,
        'desc': description
    }

    def observable_gauge_func(_):
        yield Observation(_current_gauge_values[name]['val'])

    get_otel_meter().create_observable_gauge(
        name = name,
        description = description,
        callbacks=[observable_gauge_func]
    )

    return Gauge(
        name,
        description
    )

def set_gauge(gauge, value):
    match = re.search(_numeric_value_pattern, "{}".format(value))

    if match:
        val = float(match.group())
        gauge.set(val)
        _current_gauge_values[gauge._name]['val'] = val
