from random import randint

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handle_404(request, _file_name: str = None) -> ResponseT:
    url = request.path
    pin = randint(1, 1000)
    base = read_static("_base.html")
    base_html = base.content.decode()

    body_404 = read_static("not_found.html").content.decode()
    not_found_html = body_404.format(
        url=url, pin=pin, headers_table=request_headers_print(request)
    )

    payload = base_html.format(
        favicon="favicon_red.ico", styles="style_404.css", body=not_found_html
    )
    payload = payload.encode()
    status = build_status(404)
    headers = {
        "Content-type": base.content_type,
    }

    return ResponseT(status, headers, payload)


def request_headers_print(request: RequestT) -> str:

    table_headers = ""
    for key in sorted(request.headers):
        table_headers += """
        <tr>
            <td class="key">{key}</td>
            <td class="value">{value}</td>            
        </tr>
        """.format(
            key=key, value=request.headers[key]
        )
    return table_headers
