import json
from typing import Tuple

from framework.consts import USER_DATA
from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handle_hello(request: RequestT):
    handlers = {
        "GET": handle_hello_get,
        "POST": handle_hello_post,
    }
    handler = handlers.get(request.method)
    return handler(request)


def handle_hello_get(request: RequestT) -> ResponseT:
    assert request.method == "GET"

    base = read_static("_base.html")
    base_html = base.content.decode()
    hello_html = read_static("hello.html").content.decode()

    name, address = load_user_data()

    document = hello_html.format(
        name_handler=name or "Anon",
        name_value=name or "",
        address_handler=address or "XZ",
        address_value=address or "",
    )

    payload = base_html.format(styles="/s/hello_styles.css", body=document)
    status = build_status(200)
    headers = {
        "Content-type": base.content_type,
    }
    return ResponseT(status, headers, payload.encode())


def handle_hello_post(request):
    assert request.method == "POST"

    form_data = request.form_data
    name = form_data.get("name")
    address = form_data.get("address")

    save_user_data(name, address)

    return ResponseT(
        status=build_status(302), headers={"Location": "/hello/"}, payload=b""
    )


def save_user_data(name: str, address: str) -> None:
    d = {"name": name, "address": address}
    with USER_DATA.open("w") as fp:
        json.dump(d, fp, sort_keys=True)


def load_user_data() -> Tuple[str, str]:
    if not USER_DATA.is_file():
        return "Anon", "XZ"

    with USER_DATA.open("r") as fp:
        user_date = json.load(fp)

    return (user_date.get("name") or [None])[0], (user_date.get("address") or [None])[0]
