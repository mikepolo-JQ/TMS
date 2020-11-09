from framework.types import ResponseT
from framework.utils import read_static, build_status


def handle_index(_request) -> ResponseT:
    base_html = read_static("_base.html")
    index_html = read_static("index.html").content.decode()
    payload = base_html.content.decode().format(styles="/s/styles.css", body=index_html)
    payload = payload.encode()

    status = build_status(200)
    headers = {"Content-types": base_html.content_type, }

    return ResponseT(status, headers, payload)
