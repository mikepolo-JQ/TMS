from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from applications.blog import views

urlpatterns = [
    path("", views.AllPostView.as_view(), name="index"),
    path("new/", views.MakeNewPost.as_view(), name="new"),
    path("delete/", views.DeleteAllPost.as_view(), name='delete_all'),
    path("post/<int:pk>/", views.SinglePost.as_view(), name='post'),
    path("post/<int:pk>/update/", csrf_exempt(views.UpdatePost.as_view())),
    path("post/<int:pk>/delete/", csrf_exempt(views.DeleteSinglePost.as_view())),
]
