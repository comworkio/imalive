class ImaliveHTTPException(Exception):
    def __init__(self, status_code: int, message: dict):
        self.status_code = status_code
        self.message = message
