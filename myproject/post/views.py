from django.shortcuts import render,redirect

from .models import Post,PostComment
from .forms import CommentForm

def index(request,postId):
    post=Post.objects.get(id=postId)
    comments=PostComment.objects.filter(post=post)

    return render(request,'post/index.html',{'post':post,'comments':comments,'commentform':CommentForm()})

def comment(request,postId):
    form=CommentForm(request.POST)
    post=Post.objects.get(id=postId)


    if form.is_valid():
        postername=form.cleaned_data.get('postername')
        description=form.cleaned_data.get('description')
        comment=PostComment(commenterName=postername,
                                description=description,
                                post=post
                               )
        comment.save()

    return redirect('/posts/'+postId)
