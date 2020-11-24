from django.urls import path

from applications.main.views import index

urlpatterns = [
    path("", index, name="index"),
]
