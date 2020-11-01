from handlers.ico import handler_ico
from handlers.index import handler_index
from handlers.not_found import handler_404
from handlers.response import RequestT
from handlers.styles import handler_styles
from handlers.styles_404 import handler_styles_404

handlers = {
    "/": handler_index,
    "/styles": handler_styles,
    "/favicon.ico": handler_ico,
    "/style_404": handler_styles_404,
    # "/logo/": "logo.png",
    # "/404": "page_not_found.html",
}


def application(environ: dict, start_response):
    path = environ["PATH_INFO"]

    handler = handlers.get(path, handler_404)

    request_headers = {
        key[5:]: environ[key]
        for key in filter(lambda key: key.startswith("HTTP_"), environ)
    }

    request = RequestT(
        method=environ["REQUEST_METHOD"], headers=request_headers, path=path
    )

    response = handler(request)

    start_response(response.status, list(response.headers.items()))
    yield response.payload
