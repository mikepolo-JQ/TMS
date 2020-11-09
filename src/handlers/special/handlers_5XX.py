import sys
import traceback

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handle_error(_request: RequestT = None) -> ResponseT:
    traceback.print_exc()

    error_class, error, tb = sys.exc_info()

    filenames = "".join(
        f"""<p>File <a href="http://localhost:8000/s/{frame.f_code.co_filename}">{frame.f_code.co_filename}</a>,
            line {lineno}</p>"""
        for frame, lineno in traceback.walk_tb(tb)
    )

    document = f"""
            <h1>WASTED</h1>
            <hr>
            <p>
            {filenames}
            </p>
            <p>
            {error_class.__name__}: {error}
            </p>
        """

    base_html = read_static("_base.html")

    document = base_html.content.decode().format(styles="/s/styles.css", body=document)

    payload = document.encode()
    status = build_status(500)
    headers = {"Content-type": base_html.content_type}
    return ResponseT(status, headers, payload)
