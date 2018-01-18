from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'landing/index.html')

def registerUser(request):
    return HttpResponse("<h2>Hello World!</h2>")

def registerPage(request):
    return HttpResponse("<h2>Hello Pasa!</h2>")
