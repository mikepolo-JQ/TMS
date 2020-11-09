from framework.errors import NotFound
from framework.types import RequestT
from handlers import get_handler_and_kwargs
from handlers import special


def application(environ: dict, start_response):

    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]
    query = environ.get("QUERY_STRING")
    handler, kwargs = get_handler_and_kwargs(path)

    request_headers = {
        key[5:]: environ[key]
        for key in filter(lambda key: key.startswith("HTTP_"), environ)
    }

    request = RequestT(
        method=method,
        kwargs=kwargs,
        headers=request_headers,
        path=path,
        query=query,
    )
    try:
        response = handler(request)

    except NotFound:
        response = special.handle_404(request)

    except Exception:
        response = special.handle_error()

    start_response(response.status, list(response.headers.items()))
    yield response.payload
