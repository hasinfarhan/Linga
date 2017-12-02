from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h2>Hello World!</h2>")
    return render(request, 'landing/index.html')    
