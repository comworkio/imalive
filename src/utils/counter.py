from utils.otel import get_otel_meter

def create_counter(name, description):
    return get_otel_meter().create_counter(
        name = name,
        description = description,
        unit = "1"
    )

def increment_counter(counter, tid):
    counter.add(1, {"tid": tid})
