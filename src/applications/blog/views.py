from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import UpdateView


from applications.blog.models import Post


class AllPostView(ListView):
    template_name = "blog/index.html"
    model = Post


class MakeNewPost(CreateView):

    success_url = reverse_lazy("index")
    fields = ["content", "title"]
    model = Post

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user

        return super().form_valid(form)


class DeleteAllPost(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        Post.objects.all().delete()
        return reverse_lazy("index")


class SinglePost(DetailView):
    model = Post
    template_name = "blog/post.html"


class SingleUpdate(DetailView):
    model = Post
    template_name = "blog/post_update.html"


class UpdatePost(UpdateView):
    model = Post
    fields = ["content", "title"]

    def get_success_url(self):
        success_url = reverse_lazy("post", kwargs={"pk": self.object.pk})
        return success_url


class DeleteSinglePost(DeleteView):
    http_method_names = ["post"]
    model = Post
    success_url = reverse_lazy("index")


class LikePost(View):
    def post(self, request, *args, **kwargs):
        payload = {"ok": False, "nr_likes": 0, "reason": "unknown reason"}
        pk = self.kwargs.get("pk")
        user = self.request.user
        if user.is_anonymous:
            return JsonResponse({"reason": "you is anon"})
        post = Post.objects.filter(pk=pk, who_likes=user)

        if not post:
            post = Post.objects.get(pk=pk)

            post.who_likes.add(user)
            post.save()

            post.nr_like += 1
            post.save()
            post = Post.objects.get(pk=pk)

            payload.update({"ok": True, "nr_likes": post.nr_like, "reason": None})
        else:
            payload.update({"reason": "post not found or you have liked it before"})

        return JsonResponse(payload)
