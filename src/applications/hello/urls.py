from django.urls import path

from applications.hello.views import view_hello
from applications.hello.views import view_hello_greet
from applications.hello.views import view_hello_reset

urlpatterns = [
    path("", view_hello),
    path("greet/", view_hello_greet),
    path("reset/", view_hello_reset),
]
