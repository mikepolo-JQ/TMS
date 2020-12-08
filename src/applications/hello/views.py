from django import forms
from django.views.generic import FormView
from django.views.generic import RedirectView


class HelloForm(forms.Form):
    name = forms.CharField(required=False)
    address = forms.CharField(required=False)


class HelloView(FormView):
    template_name = "hello/index.html"
    form_class = HelloForm
    success_url = "/hello/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        name = self.request.session.get("name")
        address = self.request.session.get("address")

        context.update({"ico": "g", "page": "hello", "name": name, "address": address})
        return context

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        address = form.cleaned_data["address"]
        self.request.session["name"] = name
        self.request.session["address"] = address
        return super().form_valid(form)


class HelloClearView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        self.request.session.clear()
        return "/hello/"
