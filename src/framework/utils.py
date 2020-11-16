import http
import mimetypes
from http.cookies import SimpleCookie
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Optional
from urllib.parse import parse_qs

from framework import settings
from framework.consts import DIR_STATIC, USER_TTL
from framework.consts import USER_COOKIE
from framework.errors import NotFound
from framework.types import StaticT


def get_request_headers(environ: dict) -> dict:
    headers = {
        key[5:]: environ[key]
        for key in filter(lambda key: key.startswith("HTTP_"), environ)
    }
    return headers


def get_query(environ: dict) -> dict:
    query_string = environ.get("QUERY_STRING")
    qs = parse_qs(query_string or "")
    return qs


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


def get_body(environ: dict) -> bytes:
    body = environ.get("wsgi.input")
    length = int(environ.get("CONTENT_LENGTH") or 0)

    if not length:
        return b""

    content = body.read(length)
    return content


def get_form_data(body: bytes) -> Dict[str, Any]:
    fd = body.decode()
    form_data = parse_qs(fd or "")
    return form_data


def get_user_id(headers: Dict) -> Optional[str]:
    cookies_header = headers.get("COOKIE", "")

    cookies = SimpleCookie(cookies_header)

    if USER_COOKIE not in cookies:
        return None

    user_id = cookies[USER_COOKIE].value
    return user_id


def build_user_cookie_header(user_id: str, clear=False) -> str:
    jar = SimpleCookie()

    jar[USER_COOKIE] = user_id

    cookie = jar[USER_COOKIE]
    cookie["Domain"] = settings.HOST
    cookie["Path"] = "/"
    cookie["HttpOnly"] = True

    max_age = 0 if clear else USER_TTL.total_seconds()
    cookie["Max-Age"] = max_age

    header = str(jar).split(":")[1].strip()
    return header
