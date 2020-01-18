from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.core.mail import send_mail
from django.conf import settings

from post.models import Post, PostImage

from .forms import RegisterForm
from .forms import DetailedPost
from .forms import SearchForm
from .forms import MoneyBag, LoginForm, phone, passport, nid

from .models import Profile



def index(request):
    newposts = Post.objects.all()[:5]
    mailid = request.session['mailid']
    posts = Post.objects.filter(mailid=mailid)[:3]
    detailedPost = DetailedPost()
    detailedPost.fields['postername'].initial = request.session['name']
    detailedPost.fields['mailid'].initial = mailid
    detailedPost.fields['mobilenumber'].initial = request.session['contactnumber']
    detailedPost.fields['location'].initial = request.session['primaryaddress']

    return render(request, 'landing/index.html',
                  {'post': posts, 'loginForm': LoginForm(), 'registerForm': RegisterForm(),
                   'detailedPost': detailedPost, 'searchForm': SearchForm(), 'newposts': newposts,
                   'moneybag': MoneyBag(), 'phone': phone(), 'passport': passport(), 'nid': nid()
                   })


def detailedProfile(request, userID):
    userpro = Profile.objects.get(id=userID)
    posts = Post.objects.filter(mailid=userpro.mailid)
    return render(request, 'landing/pageprofile.html',
                  {'registerForm': RegisterForm(), 'detailedPost': DetailedPost(), 'loginForm': LoginForm(),
                   'post': posts, 'searchForm': SearchForm(), 'userpro': userpro})


def loginUser(request):
    newposts = Post.objects.all()[:5]
    form = LoginForm(request.POST)
    if form.is_valid():
        mailid = form.cleaned_data.get('mailid')
        password1 = form.cleaned_data.get('password1')
        thisprofile = Profile.objects.get(mailid=mailid)
        request.session['name'] = thisprofile.accountname
        request.session['primaryaddress'] = thisprofile.primaryaddress
        request.session['contactnumber'] = thisprofile.contactnumber
        request.session['mailid'] = thisprofile.mailid
        request.session['id'] = thisprofile.id
        return redirect('/')

    return render(request, 'landing/index.html',
                  {'searchForm': SearchForm(), 'registerForm': RegisterForm(), 'detailedPost': DetailedPost(),
                   'loginForm': form, 'newposts': newposts})


def logoutUser(request):
    request.session['name'] = ""
    request.session['primaryaddress'] = ""
    request.session['contactnumber'] = ""
    request.session['mailid'] = ""
    request.session['id'] = ""

    return redirect('/')


def registerUser(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        print("kkk")
        mailid = form.cleaned_data.get('mailid')
        password1 = form.cleaned_data.get('password1')
        accountname = form.cleaned_data.get('accountname')
        primaryaddress = form.cleaned_data.get('primaryaddress')
        contactnumber = form.cleaned_data.get('contactnumber')
        newuser = Profile(mailid=mailid, password1=password1, accountname=accountname, primaryaddress=primaryaddress,
                          contactnumber=contactnumber)
        newuser.save()
        request.session['name'] = newuser.accountname
        request.session['primaryaddress'] = newuser.primaryaddress
        request.session['contactnumber'] = newuser.contactnumber
        request.session['mailid'] = newuser.mailid
        request.session['id'] = newuser.id
        return redirect('/')

    return render(request, 'landing/index.html',
                  {'registerForm': form, 'detailedPost': DetailedPost(), 'loginForm': LoginForm()})


def doSearch(request):
    form = SearchForm(request.POST)
    token = ""
    if form.is_valid():
        searchStr = form.cleaned_data.get('searchDetail')

        for c in searchStr:
            if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
                token += c
            else:
                token += '_'

    if token == "":
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponseRedirect("/searchresults/posts/" + token)


def createPost(request):
    form = DetailedPost(request.POST, request.FILES)
    if form.is_valid():
        mailid = form.cleaned_data.get('mailid')
        status = form.cleaned_data.get('status')
        postername = form.cleaned_data.get('postername')
        mobilenumber = form.cleaned_data.get('mobilenumber')
        location = form.cleaned_data.get('location')
        date = form.cleaned_data.get('fdate')
        time = form.cleaned_data.get('time')
        defintion = form.cleaned_data.get('definition')
        description = form.cleaned_data.get('description')
        # post_count=DummyPost.objects.filter().count()

        newpost = Post(mailid=mailid, status=status, posterName=postername, mobileNumber=mobilenumber,
                       location=location, defintion=defintion,
                       description=description,
                       date=date, time=time
                       )
        newpost.save()
        for f in request.FILES.getlist('image'):
            curimg = PostImage(imagefile=f, post=newpost)
            curimg.save()

        postId = str(newpost.id)

        subject = "Your post has been Acknowledged."
        message = "Hi, " + newpost.posterName + "! " + "Your " + newpost.get_status() + " post at https://www.LinGa.com has been successfully published! You can view the post at http://localhost:8000/posts/" + str(
            newpost.id) + " .You can visit it to search for new feedbacks there. Best of luck!"

        from_email = settings.EMAIL_HOST_USER
        to_email = [newpost.mailid]
        send_mail(subject, message, from_email, to_email, fail_silently=True)

        return redirect('/posts/' + postId)

    return render(request, 'landing/postfeed.html', {'messg': "Something Went Wrong"})


def createmoneybagPost(request):
    form = MoneyBag(request.POST)
    if form.is_valid():
        mailid = form.cleaned_data.get('mailid')
        status = form.cleaned_data.get('status')
        postername = form.cleaned_data.get('postername')
        mobilenumber = form.cleaned_data.get('mobilenumber')
        location = form.cleaned_data.get('location')
        dat = datetime.today().strftime('%Y-%m-%d')
        tim = datetime.now().strftime("%H:%M:%S")
        defintion = 'moneybag'
        description = form.cleaned_data.get('color')

        newpost = Post(mailid=mailid, status=status, posterName=postername, mobileNumber=mobilenumber,
                       location=location, defintion=defintion,
                       description=description,
                       date=dat, time=tim
                       )
        newpost.save()

        postId = str(newpost.id)

        subject = "Your post has been Acknowledged."
        message = "Hi, " + newpost.posterName + "! " + "Your " + newpost.get_status() + " post at https://www.LinGa.com has been successfully published! You can view the post at http://localhost:8000/posts/" + str(
            newpost.id) + " .You can visit it to search for new feedbacks there. Best of luck!"

        from_email = settings.EMAIL_HOST_USER
        to_email = [newpost.mailid]
        send_mail(subject, message, from_email, to_email, fail_silently=True)

        return redirect('/posts/' + postId)

    return render(request, 'landing/postfeed.html', {'messg': "Something Went Wrong"})


def createphoneLostPost(request):
    form = phone(request.POST)
    if form.is_valid():
        mailid = form.cleaned_data.get('mailid')
        status = form.cleaned_data.get('status')
        postername = form.cleaned_data.get('postername')
        mobilenumber = form.cleaned_data.get('mobilenumber')
        location = form.cleaned_data.get('location')
        dat = datetime.today().strftime('%Y-%m-%d')
        tim = datetime.now().strftime("%H:%M:%S")
        defintion = 'phone'
        description = form.cleaned_data.get('brand')

        newpost = Post(mailid=mailid, status=status, posterName=postername, mobileNumber=mobilenumber,
                       location=location, defintion=defintion,
                       description=description,
                       date=dat, time=tim

                       )
        newpost.save()

        postId = str(newpost.id)

        subject = "Your post has been Acknowledged."
        message = "Hi, " + newpost.posterName + "! " + "Your " + newpost.get_status() + " post at https://www.LinGa.com has been successfully published! You can view the post at http://localhost:8000/posts/" + str(
            newpost.id) + " .You can visit it to search for new feedbacks there. Best of luck!"

        from_email = settings.EMAIL_HOST_USER
        to_email = [newpost.mailid]
        send_mail(subject, message, from_email, to_email, fail_silently=True)

        return redirect('/posts/' + postId)

    return render(request, 'landing/postfeed.html', {'messg': "Something Went Wrong"})


def createpassportLostPost(request):
    form = passport(request.POST)
    if form.is_valid():
        mailid = form.cleaned_data.get('mailid')
        status = form.cleaned_data.get('status')
        postername = form.cleaned_data.get('postername')
        mobilenumber = form.cleaned_data.get('mobilenumber')
        location = form.cleaned_data.get('location')
        dat = datetime.today().strftime('%Y-%m-%d')
        tim = datetime.now().strftime("%H:%M:%S")
        defintion = 'passport'
        description = form.cleaned_data.get('country')

        newpost = Post(mailid=mailid, status=status, posterName=postername, mobileNumber=mobilenumber,
                       location=location, defintion=defintion,
                       description=description,
                       date=dat, time=tim
                       )
        newpost.save()

        postId = str(newpost.id)

        subject = "Your post has been Acknowledged."
        message = "Hi, " + newpost.posterName + "! " + "Your " + newpost.get_status() + " post at https://www.LinGa.com has been successfully published! You can view the post at http://localhost:8000/posts/" + str(
            newpost.id) + " .You can visit it to search for new feedbacks there. Best of luck!"

        from_email = settings.EMAIL_HOST_USER
        to_email = [newpost.mailid]
        send_mail(subject, message, from_email, to_email, fail_silently=True)

        return redirect('/posts/' + postId)

    return render(request, 'landing/postfeed.html', {'messg': "Something Went Wrong"})


def createnidLostPost(request):
    form = nid(request.POST)
    if form.is_valid():
        mailid = form.cleaned_data.get('mailid')
        status = form.cleaned_data.get('status')
        postername = form.cleaned_data.get('postername')
        mobilenumber = form.cleaned_data.get('mobilenumber')
        location = form.cleaned_data.get('location')
        dat = datetime.today().strftime('%Y-%m-%d')
        tim = datetime.now().strftime("%H:%M:%S")
        defintion = 'nid'
        description = form.cleaned_data.get('country')

        newpost = Post(mailid=mailid, status=status, posterName=postername, mobileNumber=mobilenumber,
                       location=location, defintion=defintion,
                       description=description, date=dat, time=tim

                       )
        newpost.save()

        postId = str(newpost.id)

        subject = "Your post has been Acknowledged."
        message = "Hi, " + newpost.posterName + "! " + "Your " + newpost.get_status() + " post at https://www.LinGa.com has been successfully published! You can view the post at http://localhost:8000/posts/" + str(
            newpost.id) + " .You can visit it to search for new feedbacks there. Best of luck!"

        from_email = settings.EMAIL_HOST_USER
        to_email = [newpost.mailid]
        send_mail(subject, message, from_email, to_email, fail_silently=True)

        return redirect('/posts/' + postId)

    return render(request, 'landing/postfeed.html', {'messg': "Something Went Wrong"})
