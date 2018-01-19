from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegisterForm
from .forms import DetailedPost

from post.models import Post

def index(request):
    return render(request,'landing/index.html',{'registerForm':RegisterForm(),'detailedPost':DetailedPost()})

def registerUser(request):
    form=RegisterForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data.get('mailid'))
        print(form.cleaned_data.get('status'))
        print(form.cleaned_data.get('postername'))
        print(form.cleaned_data.get('mobilenumber'))
        print(form.cleaned_data.get('location'))
    return render(request,'landing/index.html',{'registerForm':RegisterForm()})

def registerPage(request):
    return HttpResponse("<h2>Hello Pasa!</h2>")

def createPost(request):

    form=DetailedPost(request.POST)
    if form.is_valid():
        print(form.cleaned_data.get('date'))
        print(form.cleaned_data.get('time'))
    return render(request,'landing/postfeed.html')
