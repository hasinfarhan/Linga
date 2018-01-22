from django.shortcuts import render

from landing.forms import SearchForm
from post.models import Post

def NormalValidator(value):
    normal = ['a','an','the','on','up','in','out','do','while','of','up','about','time','over',
                            'to','from','than','that','what','into','bad','was','is','am','with','ago','recent','very','much',
                            'cost','or','else','if','you','i','u','they','he','she','end','doing','cut','person','interest',
                            'away','wait','again','before','less','more'
                           ]

    if value.lower() in normal:
        return True
    return False



def index(request,tokenHash):

    tokens=tokenHash.split("_")
    post=Post.objects.all()


    for s in tokens:
        if not NormalValidator(s):
            print(tokenHash)


    #comments=PostComment.objects.filter()





    return render(request,'searchEngine/index.html',{'searchForm':SearchForm(),'tokenstr':tokenHash,'post':post})


def profiles(request,tokenHash):

    tokens=tokenHash.split("_")
    newposts=Post.objects.all()

    for s in tokens:
        if not NormalValidator(s):
            print("mara"+tokenHash)


    #comments=PostComment.objects.filter()





    return render(request,'searchEngine/profiles.html',{'searchForm':SearchForm(),'tokenstr':tokenHash})
