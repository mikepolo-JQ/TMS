from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from applications.blog.models import Post


def index(request):
    context = {"ico": "g", "page": "blog", "object_list": Post.objects.all()}

    payload = render(request, "blog/blog.html", context=context)

    return HttpResponse(payload)


def create_new_post(request):

    title = request.POST.get("title")
    content = request.POST.get("content")

    post = Post(title=title, content=content)
    post.save()

    return redirect("/blog/")


def reset_all_posts(request):

    Post.objects.all().delete()

    return redirect("/blog/")
