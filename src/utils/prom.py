import re

from prometheus_client import Gauge

_numeric_value_pattern = r"-?\d+\.\d+"

def create_gauge(name, description):
    return Gauge(
        name,
        description
    )

def set_gauge(gauge, value):
    match = re.search(_numeric_value_pattern, "{}".format(value))

    if match:
        gauge.set(float(match.group()))
