import re
from typing import Dict
from typing import Tuple

from framework.types import HandlerT
from handlers import special
from handlers.hello import handle_hello, handler_hello_delete
from handlers.index import handle_index


def make_error(_request):
    1 / 0


urlpatterns: Dict[re.compile, HandlerT] = {
    re.compile(_path_pattern): _handler
    for _path_pattern, _handler in {
        "^/$": handle_index,
        "^/e/$": make_error,
        "^/hello/$": handle_hello,
        "^/s/(?P<file_name>.+)$": special.handle_static,
        "^/hello/delete$": handler_hello_delete,
    }.items()
}


def get_handler_and_kwargs(path: str) -> Tuple[HandlerT, dict]:
    handler = special.handle_404
    kwargs = {}

    for current_path_regex, current_handler in urlpatterns.items():
        if match := current_path_regex.match(path):
            handler = current_handler
            kwargs = match.groupdict()
            break

    return handler, kwargs
