from framework.errors import NotFound
from framework.types import RequestT
from framework.utils import get_body
from framework.utils import get_form_data
from framework.utils import get_query
from framework.utils import get_request_headers
from handlers import get_handler_and_kwargs
from handlers import special


def application(environ: dict, start_response):

    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]
    query = get_query(environ)
    handler, kwargs = get_handler_and_kwargs(path)
    request_headers = get_request_headers(environ)
    body = get_body(environ)
    form_data = get_form_data(body)

    request = RequestT(
        method=method,
        kwargs=kwargs,
        headers=request_headers,
        path=path,
        query=query,
        body=body,
        form_data=form_data,
    )

    try:
        response = handler(request)

    except NotFound:
        response = special.handle_404(request)

    except Exception:
        response = special.handle_error()

    start_response(response.status, list(response.headers.items()))
    yield response.payload
