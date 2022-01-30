from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, Django here")

def sasha(request):
    return HttpResponse("Hello, Sasha")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize(),
    })
