from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegisterForm
from .forms import DetailedPost

def index(request):
    return render(request,'landing/index.html',{'registerForm':RegisterForm(),'detailedPost':DetailedPost()})

def registerUser(request):
    form=RegisterForm(request.POST);
    if form.is_valid():
        print(form.cleaned_data.get('mailid'))
    return render(request,'landing/index.html',{'registerForm':RegisterForm()})

def registerPage(request):
    return HttpResponse("<h2>Hello Pasa!</h2>")
