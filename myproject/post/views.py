from django.shortcuts import render
from .models import Post


def index(request,postId):
    post=Post.objects.get(id=postId)

    

    return render(request,'post/index.html',{'post':post})
