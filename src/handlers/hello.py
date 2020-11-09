from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handle_hello(request: RequestT):

    name = (request.form_data.get("name") or [None])[0]
    address = (request.form_data.get("address") or [None])[0]

    base_html = read_static("_base.html")
    hello_html = read_static("hello.html").content.decode()

    document = hello_html.format(
        name_handler=name or "anon",
        name_value=name or "",
        address_handler=address or "XZ",
        address_value=address or "",
    )

    payload = base_html.content.decode().format(
        styles="/s/hello_styles.css", body=document
    )
    status = build_status(200)
    headers = {
        "Content-type": base_html.content_type,
    }
    return ResponseT(status, headers, payload.encode())
