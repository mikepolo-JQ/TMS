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

        user = self.request.user

        # if user.is_anonymous:
        #     return JsonResponse({"reason": "you anon"})

        payload = {"ok": False, "nr_likes": 0, "reason": "unknown reason"}

        pk = self.kwargs.get("pk", 0)
        post = Post.objects.filter(pk=pk).first()

        if not post:
            payload.update({"reason": "post not found"})
        elif post.author == user:
            payload.update({"reason": "don't like your own posts"})
        else:
            if post.is_liked_by(user):
                post.who_likes.remove(user)
            else:
                post.who_likes.add(user)
            post.save()

            post = Post.objects.get(pk=pk)
            payload.update({"ok": True, "nr_likes": post.nr_likes, "reason": None})

        return JsonResponse(payload)


class LikeColorPost(View):
    def post(self, request, *args, **kwargs):
        payload = {"ok": False}
        list_pk = [post.pk for post in Post.objects.all()]

        my_list = []
        for pk in list_pk:
            post = Post.objects.get(pk=pk)

            if post.is_liked_by(self.request.user):
                my_list.append(pk)
                payload.update({"ok": True})

        payload.update({"posts_id": my_list})

        return JsonResponse(payload)
