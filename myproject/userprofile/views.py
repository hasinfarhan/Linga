from django.shortcuts import render
from django.http import HttpResponse

def mainprofile(request):
    return render(request,'userprofile/index.html')
