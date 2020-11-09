from urllib.parse import parse_qs

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handle_hello(request: RequestT):

    query_string = parse_qs(request.query or "")
    name = (query_string.get("name") or [None])[0]

    base_html = read_static("_base.html")
    hello_html = read_static("hello.html").content.decode()

    document = hello_html.format(
        name_handler=name or "anon",
        name_value=name or "",
    )

    payload = base_html.content.decode().format(styles="/s/styles.css", body=document)
    status = build_status(200)
    headers = {
        "Content-type": base_html.content_type,
    }
    return ResponseT(status, headers, payload.encode())
