from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hello(request: HttpRequest) -> HttpResponse:
    payload = render(
        request,
        "hello/hello.html",
        context={
            "ico": "g",
            "page": "hello",
            "name_handler": "Anon",
            "name_value": "",
            "address_handler": "XZ",
            "address_value": "",
        },
    )

    return HttpResponse(content=payload)
