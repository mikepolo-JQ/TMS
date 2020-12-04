from django import forms
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import FormView


class HelloForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()


class HelloView(FormView):
    template_name = "hello/index.html"
    success_url = "/hello/"
    form_class = HelloForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        name = self.request.session.get("name")
        address = self.request.session.get("address")

        context.update(
            {
                "ico": "g",
                "page": "hello",
                "name_handler": name or "Anon",
                "name_value": name or "",
                "address_handler": address or "XZ",
                "address_value": address or "",
            }
        )
        return context



#
#
# def view_hello_greet(request: HttpRequest):
#     name = request.POST.get("name")
#     address = request.POST.get("address")
#
#     request.session["name"] = name
#     request.session["address"] = address
#
#     return redirect("/hello/")
#
#
# def view_hello_reset(request: HttpRequest):
#     request.session.clear()
#     return redirect("/hello/")
