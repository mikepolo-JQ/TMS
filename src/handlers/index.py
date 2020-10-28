from framework.utils import read_static
from handlers.response import ResponseT


def handler_index(_environ) -> ResponseT:
    base_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()
    payload = base_html.format(styles_path="/styles", body=index_html)
    payload = payload.encode()
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    return status, headers, payload