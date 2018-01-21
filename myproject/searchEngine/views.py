from django.shortcuts import render

def index(request,tokenHash):

    return render(request,'searchEngine/index.html')
