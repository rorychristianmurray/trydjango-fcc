from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")  # string of html code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>Contact Page</h1>")


def about_view(request, *args, **kwargs):
    print(request)
    return HttpResponse("<h1>Rory... he's a cool guy, I've heard")
