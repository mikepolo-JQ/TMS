from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from applications.blog.models import Post


class AllPostView(ListView):
    template_name = "blog/blog.html"
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        context.update(
            {"ico": "g", "page": "blog"}
        )
        return context


class MakeNewPost(CreateView):

    success_url = "/blog/"
    fields = ["content", "title"]
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        context.update(
            {"ico": "g", "page": "blog"}
        )
        return context


# def index(request):
#     context = {"ico": "g", "page": "blog", "object_list": Post.objects.all()}
#
#     payload = render(request, "blog/blog.html", context=context)
#
#     return HttpResponse(payload)
#
#
# def create_new_post(request):
#
#     title = request.POST.get("title")
#     content = request.POST.get("content")
#
#     post = Post(title=title, content=content)
#     post.save()
#
#     return redirect("/blog/")
#
#
# def reset_all_posts(request):
#
#     Post.objects.all().delete()
#
#     return redirect("/blog/")
