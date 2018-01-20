from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegisterForm
from .forms import DetailedPost

#from post.models import Post
from post.models import DummyPost

def index(request):
    return render(request,'landing/index.html',{'registerForm':RegisterForm(),'detailedPost':DetailedPost()})

def registerUser(request):
    form=RegisterForm(request.POST)


def registerPage(request):
    return HttpResponse("<h2>Hello Pasa!</h2>")

def createPost(request):
    form=DetailedPost(request.POST)
    if form.is_valid():
        mailid=form.cleaned_data.get('mailid')
        status=form.cleaned_data.get('status')
        postername=form.cleaned_data.get('postername')
        mobilenumber=form.cleaned_data.get('mobilenumber')
        location=form.cleaned_data.get('location')
        date=form.cleaned_data.get('date')
        time=form.cleaned_data.get('time')
        defintion=form.cleaned_data.get('definition')
        description=form.cleaned_data.get('description')
        post_count=DummyPost.objects.filter().count()

        newdummypost=DummyPost(postid=post_count+1,mailid=mailid,status=status,posterName=postername,mobileNumber=mobilenumber,location=location,defintion=defintion,
                                description=description,
                                date=date,time=time
                               )
        newdummypost.save()
        return render(request,'landing/postfeed.html',{'article':newdummypost,'messg':"Congratulations",'successbool':False})

    return render(request,'landing/postfeed.html',{'messg':"Something Went Wrong",'successbool':True})
