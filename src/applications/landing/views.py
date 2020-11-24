from random import randint

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request):
    payload = render(
        request,
        "landing/index.html",
        context={
            "ico": "g",
            "page": "index"})
    return HttpResponse(payload)


def not_found(request: HttpRequest) -> HttpResponse:

    url = request.path
    pin = randint(1, 1000)

    payload = render(
        request,
        "404.html",
        context={
            "ico": "r",
            "page": "not_found",
            "url": url,
            "pin": pin,
            "request_headers": request.headers,
        },
    )
    return HttpResponse(payload, status=404)
