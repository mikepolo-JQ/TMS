from framework.utils import read_static
from handlers.response import ResponseT


def handler_styles_404(_environ) -> ResponseT:
    payload = read_static("assets/style_404.css")
    status = "200 OK"
    headers = {
        "Content-type": "text/css",
    }
    return status, headers, payload
