from framework.types import HandlerRequest
from framework.types import RequestT
from handlers.index import handler_index
from handlers.static import handler_static
from handlers.styles import handler_styles
from handlers.system_handlers.not_found import handler_404

# handlers = {
#     "/": handler_index,
#     "/styles": handler_styles,
#     "/favicon.ico": handler_ico,
#     "/style_404": handler_styles_404,
#     # "/logo/": "logo.png",
#     # "/404": "page_not_found.html",
# }

handlers = {
    "/": HandlerRequest(handler_index, "index.html"),
    "/styles": HandlerRequest(handler_styles, "styles.css"),
    "/favicon.ico": HandlerRequest(handler_static, "favicon.ico"),
    "/style_404": HandlerRequest(handler_styles, "style_404.css"),
    # "/logo/": "logo.png",
}


def application(environ: dict, start_response):
    path = environ["PATH_INFO"]

    handler_info = handlers.get(path, HandlerRequest(handler_404, ""))

    request_headers = {
        key[5:]: environ[key]
        for key in filter(lambda key: key.startswith("HTTP_"), environ)
    }

    request = RequestT(
        method=environ["REQUEST_METHOD"], headers=request_headers, path=path
    )

    response = handler_info.handler(request, handler_info.file_name)

    start_response(response.status, list(response.headers.items()))
    yield response.payload
