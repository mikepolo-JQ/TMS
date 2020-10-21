import mimetypes

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]
    if url == "/new_list/":
        status = "200 OK"
        text_css_content_type = mimetypes.guess_type("text.css")
        headers = {
            "Content-type": text_css_content_type[0],
        }
        payload = read_from_styles_css()
        start_response(status, list(headers.items()))

        yield payload

    elif url == "/logo.png/":
        status = "200 OK"
        logo_content_type = mimetypes.guess_type("logo.png")
        headers = {
            "Content-type": logo_content_type[0],
        }
        payload = read_from_logo_png()
        start_response(status, list(headers.items()))
        yield payload

    else:
        status = "200 OK"
        text_html_content_type = mimetypes.guess_type("text.html")
        headers = {
            "Content-type": text_html_content_type[0],
        }
        payload = read_from_index_html()

        start_response(status, list(headers.items()))
        yield payload


def read_from_index_html():
    path = DIR_STATIC / "index.html"

    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    return payload


def read_from_styles_css():
    path = DIR_STATIC / "styles.css"

    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    return payload


def read_from_logo_png():
    path = DIR_STATIC / "logo.png"

    with path.open("rb") as fp:
        payload = fp.read()

    return payload
