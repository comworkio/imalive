from uuid import uuid4
from asgi_correlation_id import correlation_id

from utils.common import is_empty

def get_current_cid():
    try:
        cid = correlation_id.get()
        if is_empty(cid):
            cid = "{}".format(uuid4())
        return cid
    except Exception:
        return "{}".format(uuid4())
