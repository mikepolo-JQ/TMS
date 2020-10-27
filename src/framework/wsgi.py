from mimetypes import guess_type

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handlers = {
        "/": handler_index,
        # "/styles": "assets/styles.css",
        # "/logo/": "logo.png",
        # "/favicon.ico": "favicon.ico",
        # "/style_404": "assets/style_404.css",
        # "/404": "page_not_found.html",
    }

    handler = handlers.get(url, handler_404)
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    payload = handler(environ)

    start_response(status, list(headers.items()))
    yield payload


def handler_index(_environ) -> bytes:
    base_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()
    result = base_html.format(body=index_html)

    return result.encode()


def handler_404(environ) -> bytes:
    url = environ["PATH_INFO"]
    base_html = read_static("_base.html").decode()
    body_404 = f"""
            <div class="header">
                <div class="container">
                    <div class="header__inner">
                        <div class="header__logo">MiPo</div>
        
                        <nav class="nav">
                            <a class="nav__link" href="#">About</a>
                            <a class="nav__link" href="#">Service</a>
                            <a class="nav__link" href="#">Work</a>
                            <a class="nav__link" href="#">Block</a>
                            <a class="nav__link" href="#">Contact</a>
                        </nav>
                    </div>
                </div>
            </div>
        
            <div class="intro">
                <div class="container">
                    <div class="intro_inner">
                        <h2 class="intro__suptitle">Ooops...</h2>
                        <h1 class="intro__title">Your path {url} not found</h1>
        
                        <a href="/" class="button">< Go home</a>
                    </div>
                </div>
        
            </div>"""
    result = base_html.format(body=str(body_404))
    return result.encode()


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name

    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def generate_status() -> str:
    pass


# def generate_404(environ) -> bytes:
#
#     url = environ["PATH_INFO"]
#     pin = random.randint(1, 1000)
#
#     msg = f"Hello, bro. Your path: {url} is not found. Pin: {pin}"
#     return msg.encode()
