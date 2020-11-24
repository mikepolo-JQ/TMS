from random import randint

from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include
from django.urls import path


def not_found(request: HttpRequest) -> HttpResponse:

    url = request.path
    pin = randint(1, 1000)
    context = {
        "ico": "r",
        "page": "not_found",
        "url": url,
        "pin": pin,
        "request_headers": request.headers,
    }

    payload = render(
        request,
        "404.html",
        context=context,
    )

    return HttpResponse(payload, status=404)


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include("applications.landing.urls"), name="index"),
    path("hello/", include("applications.hello.urls"), name="hello"),
    path("learnMore/", not_found, name="not_found"),
]
