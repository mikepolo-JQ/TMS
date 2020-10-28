from handlers.ico import handler_ico
from handlers.index import handler_index
from handlers.not_found import handler_404
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


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handler = handlers.get(url, handler_404)

    status, headers, payload = handler(environ)

    start_response(status, list(headers.items()))
    yield payload
