from django.shortcuts import render,redirect

from .models import Post,PostComments
from .forms import CommentForm

def index(request,postId):
    post=Post.objects.get(id=postId)
    return render(request,'post/index.html',{'post':post,'commentform':CommentForm()})

def comment(request,postId):
    form=CommentForm(request.POST)
    post=Post.objects.get(id=postId)


    if form.is_valid():
        postername=form.cleaned_data.get('postername')
        description=form.cleaned_data.get('description')
        #newcomment=Post(commenterName=postername,
                                #description=description
                               #)
        #newcomment.save()


    return redirect('/posts/'+postId)
