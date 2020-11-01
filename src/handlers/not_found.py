from random import randint

from framework.utils import read_static
from handlers.response import RequestT
from handlers.response import ResponseT


def handler_404(request) -> ResponseT:
    url = request.path
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
            
            </div>

            <div class="headers"> 
                <div class="container">
                    <h2 class="header_h2">Headers</h2>
                    <table>
                        {request_headers_print(request)}
                     </table>                    
                </div>
            </div>"""

    payload = base_html.format(styles="/style_404", body=str(body_404))
    payload = payload.encode()
    status = "404 Not Found"
    headers = {
        "Content-type": "text/html",
    }

    return ResponseT(status, headers, payload)


def request_headers_print(request: RequestT) -> str:

    header = """
        <tr>
            <td class="key">{key}</td>
            <td class="value">{value}</td>            
        </tr>
        """
    table_headers = ""
    for key in sorted(request.headers):
        table_headers += header.format(key=key, value=request.headers[key])
    return table_headers
