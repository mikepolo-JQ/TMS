from django.urls import path

from applications.hello import views

urlpatterns = [
    path("", views.HelloView.as_view(), name="hello"),
    path("reset/", views.HelloClearView.as_view()),
]
