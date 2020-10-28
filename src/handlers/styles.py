from framework.utils import read_static
from handlers.response import ResponseT


def handler_styles(_environ) -> ResponseT:
    payload = read_static("assets/styles.css")
    status = "200 OK"
    headers = {
        "Content-type": "text/css",
    }
    return status, headers, payload
