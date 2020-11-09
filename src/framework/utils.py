import http
import mimetypes
from pathlib import Path

from framework.consts import DIR_STATIC
from framework.errors import NotFound
from framework.types import StaticT


def read_static(file_name: str) -> StaticT:
    if file_name.startswith("/"):
        file_obj = Path(file_name).resolve()
    else:
        file_obj = (DIR_STATIC / file_name).resolve()

    if not file_obj.exists():
        raise NotFound

    with file_obj.open("rb") as fp:
        content = fp.read()

    content_type = mimetypes.guess_type(file_name)[0]

    return StaticT(content=content, content_type=content_type)


def build_status(code: int) -> str:
    status = http.HTTPStatus(code)
    reason = "".join(word.capitalize() for word in status.name.split("_"))

    text = f"{code} {reason}"
    return text
