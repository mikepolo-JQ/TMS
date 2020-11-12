from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handle_index(_request) -> ResponseT:
    base_html = read_static("_base.html")
    index_html = read_static("index.html").content.decode()
    payload = base_html.content.decode().format(
        favicon="favicon.ico", styles="styles.css", body=index_html
    )
    payload = payload.encode()

    status = build_status(200)
    headers = {
        "Content-types": base_html.content_type,
    }

    return ResponseT(status, headers, payload)
