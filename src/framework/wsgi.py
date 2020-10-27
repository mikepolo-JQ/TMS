import random
from mimetypes import guess_type

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]

    file_names = {
        "/styles": "assets/styles.css",
        "/logo/": "logo.png",
        "/": "index.html",
        "/favicon.ico": "favicon.ico",
        "/style_404": "assets/style_404.css",
        "/404": "page_not_found.html"
    }

    file_name = file_names.get(url, "page_not_found.html")
    status = generate_status(file_name)
    headers = {
        "Content-type": guess_type(file_name)[0],
    }
    payload = read_static(file_name)

    start_response(status, list(headers.items()))
    yield payload


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name

    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def generate_status(file_name: str) -> str:
    if file_name == "page_not_found.html":
        return "404 NOT FOUND"
    return "200 OK"


# def generate_404(environ) -> bytes:
#
#     url = environ["PATH_INFO"]
#     pin = random.randint(1, 1000)
#     msg = f"Hello, bro. Your path: {url} is not found. Pin: {pin}"
#     return msg.encode()
