from random import randint

from framework.utils import read_static
from handlers.response import ResponseT


def handler_404(environ) -> ResponseT:
    url = environ["PATH_INFO"]
    pin = randint(1, 1000)
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
                        <h1 class="intro__title">Your path 
                            <span class="url">{url}</span> 
                            not found. 
                            <span class="pin">Pin: {pin}</span>
                            </h1>                           
        
                        <a href="/" class="button">< Go home</a>
                    </div>
                </div>
        
            </div>"""
    payload = base_html.format(styles_path="/style_404", body=str(body_404))
    payload = payload.encode()
    status = "404 Not Found"
    headers = {
        "Content-type": "text/html",
    }

    return status, headers, payload
