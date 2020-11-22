from random import randint

from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def index(request):
    payload = render(request, "index.html", context={"page": "index"})
    return HttpResponse(payload)


def hello(request: HttpRequest) -> HttpResponse:
    payload = render(
        request,
        "hello.html",
        context={
            "page": "hello",
            "name_handler": "Anon",
            "name_value": "",
            "address_handler": "XZ",
            "address_value": "",
        },
    )

    return HttpResponse(content=payload)


def not_found(request: HttpRequest) -> HttpResponse:

    url = request.path
    pin = randint(1, 1000)

    payload = render(
        request,
        "not_found.html",
        context={
            "page": "not_found",
            "url": url,
            "pin": pin,
            "request_headers": request.headers,
        },
    )
    return HttpResponse(payload, status=404)


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", index, name="index"),
    path("hello/", hello, name="hello"),
    path("learnMore/", not_found, name="not_found"),
]
