from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("<h1 style='color:red;'>Welcome to Home Page</h1>")
    return render(request, 'index.html', {})

def about(request):
    # return HttpResponse("<h1 style='color:green;'>Welcome to About Us Page</h1>")
    # HttpResponse() to display a message render() to display an HTML
    return render(request, 'about.html', {})