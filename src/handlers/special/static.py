from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handle_static(request: RequestT) -> ResponseT:

    file_name = request.kwargs["file_name"]
    static = read_static(file_name)

    status = build_status(200)
    headers = {
        "Content-type": static.content_type,
    }
    return ResponseT(status, headers, static.content)
