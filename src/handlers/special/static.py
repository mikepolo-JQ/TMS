from framework.types import ResponseT, RequestT
from framework.utils import read_static, build_status


def handle_static(request: RequestT) -> ResponseT:

    file_name = request.kwargs["file_name"]
    static = read_static(file_name)

    status = build_status(200)
    headers = {
        "Content-type": static.content_type,
    }
    return ResponseT(status, headers, static.content)
