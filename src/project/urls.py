from random import randint

from django.conf.urls import handler404
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include
from django.urls import path
from django.views.defaults import ERROR_404_TEMPLATE_NAME


def view_not_found(request, exception, template_name=ERROR_404_TEMPLATE_NAME):

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


handler404 = view_not_found

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include("applications.main.urls"), name="index"),
    path("hello/", include("applications.hello.urls"), name="hello"),
]
