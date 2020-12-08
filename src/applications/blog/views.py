from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic import RedirectView


from applications.blog.models import Post


class AllPostView(ListView):
    template_name = "blog/index.html"
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        context.update({"ico": "g", "page": "blog"})
        return context


class MakeNewPost(CreateView):

    success_url = reverse_lazy("index")
    fields = ["content", "title"]
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        context.update({"ico": "g", "page": "blog"})
        return context


class DeleteAllPost(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        Post.objects.all().delete()
        return reverse_lazy("index")


class SinglePost(DetailView):
    model = Post
    template_name = "blog/post.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        context.update({"ico": "g", "page": "blog"})
        return context


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


