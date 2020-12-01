from django.urls import path

from applications.blog import views

urlpatterns = [
    path("", views.index),
    path("new/", views.create_new_post),
    path("delete/", views.reset_all_posts),
]
