from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        context = {"ico": "g", "page": "index"}

        payload = render(self.request, "main/index.html", context=context)

        return payload

