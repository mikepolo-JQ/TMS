from django.urls import path

from applications.blog import views

urlpatterns = [
    path("", views.AllPostView.as_view()),
    path("new/", views.MakeNewPost.as_view()),
    path("delete/", views.DeleteAllPost.as_view()),
]
