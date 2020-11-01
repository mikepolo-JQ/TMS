from framework.utils import read_assets
from framework.types import ResponseT
from mimetypes import guess_type


def handler_styles(_request, file_name) -> ResponseT:
    payload = read_assets(file_name)
    status = "200 OK"
    headers = {
        "Content-type": guess_type(file_name)[0],
    }
    return ResponseT(status, headers, payload)
