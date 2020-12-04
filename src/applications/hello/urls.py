from django.urls import path

from applications.hello.views import  HelloView
# from applications.hello.views import view_hello_greet
# from applications.hello.views import view_hello_reset

urlpatterns = [
    path("", HelloView.as_view()),
    # path("reset/", view_hello_reset),
]
