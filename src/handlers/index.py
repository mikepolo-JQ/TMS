from framework.types import ResponseT
from framework.utils import read_static


def handler_index(_request, _file_name) -> ResponseT:
    base_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()
    payload = base_html.format(styles="/styles", body=index_html)
    payload = payload.encode()
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    return ResponseT(status, headers, payload)
