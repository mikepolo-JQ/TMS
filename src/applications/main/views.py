from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"ico": "g", "page": "index"}

    payload = render(request, "main/index.html", context=context)

    return HttpResponse(payload)
