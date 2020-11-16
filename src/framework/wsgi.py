from framework.errors import NotFound
from framework.storage import find_user
from framework.types import RequestT
from framework.utils import get_body, get_request_method, get_request_path
from framework.utils import get_form_data
from framework.utils import get_query
from framework.utils import get_request_headers
from framework.utils import get_user_id
from handlers import get_handler_and_kwargs
from handlers import special


def application(environ: dict, start_response):

    path = get_request_path(environ)
    method = get_request_method(environ)
    query = get_query(environ)
    handler, kwargs = get_handler_and_kwargs(path)
    request_headers = get_request_headers(environ)
    body = get_body(environ)
    form_data = get_form_data(body)

    user_id = get_user_id(request_headers)
    user = find_user(user_id)

    request = RequestT(
        method=method,
        kwargs=kwargs,
        headers=request_headers,
        path=path,
        query=query,
        body=body,
        form_data=form_data,
        user=user,
    )

    try:
        response = handler(request)

    except NotFound:
        response = special.handle_404(request)

    except Exception:
        response = special.handle_error()

    start_response(response.status, list(response.headers.items()))
    yield response.payload
