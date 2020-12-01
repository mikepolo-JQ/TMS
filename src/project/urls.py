import sys
import traceback
from random import randint

from django.conf.urls import handler404
from django.conf.urls import handler500
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include
from django.urls import path
from django.views.defaults import ERROR_404_TEMPLATE_NAME
from django.views.defaults import ERROR_500_TEMPLATE_NAME
from dynaconf import settings as _ds


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


def handle_error(request, template_name=ERROR_500_TEMPLATE_NAME):
    traceback.print_exc()

    error_class, error, tb = sys.exc_info()

    context = {
        "ico": "r",
        "page": "not_found",
        "traceback": traceback.walk_tb(tb),
        "HOST": _ds.HOST,
        "error_name": error_class.__name__,
        "error": error,
    }

    payload = render(request, template_name, context=context)

    return HttpResponse(payload, status=500)


handler404 = view_not_found
handler500 = handle_error


def make_error(_request):
    1 / 0


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include("applications.main.urls"), name="index"),
    path("hello/", include("applications.hello.urls"), name="hello"),
    path("e/", make_error),
    path("blog/", include("applications.blog.urls"), name="blog"),
]
