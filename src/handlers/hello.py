from framework import settings
from framework.consts import USER_COOKIE
from framework.consts import USER_TTL
from framework.errors import MethodNotAllowed
from framework.storage import save_user, delete_cookie
from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status, build_user_cookie_header
from framework.utils import read_static


def handle_hello(request: RequestT):
    handlers = {
        "GET": handle_hello_get,
        "POST": handle_hello_post,
    }
    handler = handlers.get(request.method)
    if not handler:
        raise MethodNotAllowed

    return handler(request)


def handle_hello_get(request: RequestT) -> ResponseT:
    assert request.method == "GET"

    base = read_static("_base.html")
    base_html = base.content.decode()
    hello_html = read_static("hello.html").content.decode()

    document = hello_html.format(
        name_handler=request.user.name or "Anon",
        name_value=request.user.name or "",
        address_handler=request.user.address or "XZ",
        address_value=request.user.address or "",
    )

    payload = base_html.format(
        favicon="favicon.ico", styles="hello_styles.css", body=document
    )

    status = build_status(200)
    headers = {
        "Content-type": base.content_type,
    }
    return ResponseT(status, headers, payload.encode())


def handle_hello_post(request):
    assert request.method == "POST"

    form_data = request.form_data
    name = form_data.get("name", [None])[0]
    address = form_data.get("address", [None])[0]

    request.user.name = name
    request.user.address = address

    save_user(request.user)

    cookie = build_user_cookie_header(request.user.id)

    resp = ResponseT(
        status=build_status(302),
        headers={
            "Location": "/hello/",
            "Set-Cookie": cookie,
        },
    )

    return resp


def handler_hello_delete(request: RequestT) -> ResponseT:
    delete_cookie(request.user)

    cookie = build_user_cookie_header(request.user.id, clear=True)

    headers = {
        "Location": "/hello/",
        "Set-Cookie": cookie,
    }

    return ResponseT(
        status=build_status(302),
        headers=headers,
    )
