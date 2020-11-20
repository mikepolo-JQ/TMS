from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import path

from framework.utils import read_static
# from my_app import views


def index(request):
    payload = render(request, "index.html",
                     context={'styles': "{% static 'styles/styles.css' %}"})
    return HttpResponse(payload)


def styles(_request):
    payload = read_static("assets/styles/styles.css").content

    return HttpResponse(payload, content_type="text/css")


def hello(_request: HttpRequest) -> HttpResponse:
    base = read_static("_base.html")
    base_html = base.content.decode()
    hello_html = read_static("hello.html").content.decode()

    document = hello_html.format(
        name_handler="Anon",
        name_value="",
        address_handler="XZ",
        address_value="",
    )

    payload = base_html.format(
        favicon="favicon.ico", styles="hello_styles.css/", body=document
    ).encode()
    return HttpResponse(content=payload)


def hello_styles(_request: HttpRequest) -> HttpResponse:
    payload = read_static("assets/styles/hello_styles.css").content.decode()

    return HttpResponse(payload.encode(), content_type="text/css")


urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("", index, name='index'),

    path("hello/", hello, name='hello'),
    path('hello/s/assets/styles/hello_styles.css/', hello_styles)
]
