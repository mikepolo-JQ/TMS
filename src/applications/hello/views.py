from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render


def view_hello(request: HttpRequest) -> HttpResponse:
    name = request.session.get("name")
    address = request.session.get("address")

    context = {
        "ico": "g",
        "page": "hello",
        "name_handler": name or "Anon",
        "name_value": name or "",
        "address_handler": address or "XZ",
        "address_value": address or "",
    }

    payload = render(
        request,
        "hello/hello.html",
        context=context,
    )

    return payload


def view_hello_greet(request: HttpRequest):
    name = request.POST.get("name")
    address = request.POST.get("address")

    request.session["name"] = name
    request.session["address"] = address

    return redirect("/hello/")


def view_hello_reset(request: HttpRequest):
    request.session.clear()
    return redirect("/hello/")
