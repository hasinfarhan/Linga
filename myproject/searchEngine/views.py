from django.shortcuts import render

from landing.forms import SearchForm,FilterSearch
from post.models import Post
from landing.models import Profile




def index(request,tokenHash):

    posts=Post.objects.all()
    sorted_results = sorted(posts,key=lambda t: -t.weight_of_matches(tokenHash))

    return render(request,'searchEngine/index.html',{'searchForm':SearchForm(),'tokenstr':tokenHash,'posts':sorted_results,'filter':FilterSearch() })




def profiles(request,tokenHash):

    ppl=Profile.objects.all()
    sorted_results = sorted(ppl,key=lambda t: -t.weight_of_matches(tokenHash))



    return render(request,'searchEngine/profiles.html',{'searchForm':SearchForm(),'tokenstr':tokenHash,'ppl':sorted_results })
