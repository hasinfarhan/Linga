from django.shortcuts import render,redirect

from .models import Post,PostComment,PostImage
from .forms import CommentForm
from landing.forms import SearchForm

from django.core.mail import send_mail
from django.conf import settings

def searchFeed(request,postId):
    post=Post.objects.get(id=postId)
    tot=post.get_definition_tags()+post.get_definition_tags()


def delPost(request,postId):
    Post.objects.filter(id=postId).delete()
    return redirect("/")




def index(request,postId):
    post=Post.objects.get(id=postId)
    comments=PostComment.objects.filter(post=post)
    images=PostImage.objects.filter(post=post)
    picker=False
    if post.mailid==request.session['mailid']:
        picker=True

    return render(request,'post/index.html',{'post':post,'comments':comments,'images':images,'commentform':CommentForm(),'searchForm':SearchForm(),'picker':picker})

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

        subject="Someone commented in your post on LinGa."
        message="Hi, "+post.posterName+"! "+"Someone commented on your "+post.get_status()+" post at https://www.LinGa.com! You can view the post at http://localhost:8000/posts/"+str(post.id)+". Best of luck!"

        from_email=settings.EMAIL_HOST_USER
        to_email=[post.mailid]
        send_mail(subject,message,from_email,to_email,fail_silently=True)


    return redirect('/posts/'+postId)
