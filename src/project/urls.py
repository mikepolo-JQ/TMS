from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include("applications.landing.urls"), name="index"),
    path("hello/", include("applications.hello.urls"), name="hello"),
    # path("learnMore/", not_found, name="not_found"),
]
