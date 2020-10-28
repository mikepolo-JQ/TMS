from framework.utils import read_static
from handlers.response import ResponseT


def handler_ico(_environ) -> ResponseT:
    payload = read_static("favicon.ico")
    status = "200 OK"
    headers = {
        "Content-type": "image/ico",
    }
    return status, headers, payload
