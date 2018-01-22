from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from datetime import datetime

from .models import Profile


def ForbiddenUsernamesValidator(value):
    forbidden_usernames = ['admin', 'settings', 'news', 'about', 'help',
                           'signin', 'signup', 'signout', 'terms', 'privacy',
                           'cookie', 'new', 'login', 'logout', 'administrator',
                           'join', 'account', 'username', 'root', 'blog',
                           'user', 'users', 'billing', 'subscribe', 'reviews',
                           'review', 'blog', 'blogs', 'edit', 'mail', 'email',
                           'home', 'job', 'jobs', 'contribute', 'newsletter',
                           'shop', 'profile', 'register', 'auth',
                           'authentication', 'campaign', 'config', 'delete',
                           'remove', 'forum', 'forums', 'download',
                           'downloads', 'contact', 'blogs', 'feed', 'feeds',
                           'faq', 'intranet', 'log', 'registration', 'search',
                           'explore', 'rss', 'support', 'status', 'static',
                           'media', 'setting', 'css', 'js', 'follow',
                           'activity', 'questions', 'articles', 'network', ]

    if value.lower() in forbidden_usernames:
        raise ValidationError('This is a reserved word.')


def InvalidUsernameValidator(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('Enter a valid username.')


def UniqueEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


def UniqueUsernameIgnoreCaseValidator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this Username already exists.')



class LoginForm(forms.Form):
    mailid=forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'E-mail*','required data-validation-required-message':'Please enter a valid Email ID.'}),
        required=True,
        max_length=75,
        )
    password1=forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password*', 'required data-validation-required-message':'Please enter a Password.'}),
        required=True,
        )

    def __init__(self, *args, **kwargs):

        instance = kwargs.get('instance', None)

        kwargs.update(initial={
            # 'field': 'value'
        })

        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(LoginForm, self).clean()
        mail=self.cleaned_data.get('mailid')
        passwrd=self.cleaned_data.get('password1')



        if Profile.objects.filter(mailid=mail).count()==0:
            print("bhul1")
            raise forms.ValidationError("Sorry, the account is not registered.")

        thisprofile=Profile.objects.get(mailid=mail)
        rightpass=thisprofile.password1

        if rightpass!=passwrd:
            print("bhul2")
            raise forms.ValidationError("Sorry, the password didn't match.")


        return self.cleaned_data





class RegisterForm(forms.Form):
    mailid=forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'E-mail*','required data-validation-required-message':'Please enter a valid Email ID.'}),
        required=True,
        max_length=75,
        )
    password1=forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password*', 'required data-validation-required-message':'Please enter a Password.'}),
        required=True,
        min_length=6,
        )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password*',
                                        'data-validation-matches-match':'password1', 'data-validation-matches-message':"Passwords didn't match!",
                                         'required data-validation-required-message':"Please confirm your Password."
                                          }),
        required=True)
    accountname=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Account Name*','required data-validation-required-message':'Please enter your Account Name.'}),
        max_length=40,
        required=True,
        )
    primaryaddress=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id':'locationSearchField2','placeholder':'Primary Address'}),
        max_length=100,
        required=False
        )
    contactnumber=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Contact Number'}),
        max_length=35,
        required=False
        )


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['accountname'].validators.append(ForbiddenUsernamesValidator)
        self.fields['accountname'].validators.append(InvalidUsernameValidator)
        self.fields['accountname'].validators.append(
            UniqueUsernameIgnoreCaseValidator)
        self.fields['mailid'].validators.append(UniqueEmailValidator)

    def clean(self):
        super(RegisterForm, self).clean()
        mail= self.cleaned_data.get('mailid')
        if Profile.objects.filter(mailid=mail).count()>0:
            print("bhul3")
            raise forms.ValidationError("Sorry, that email is taken. Please try another.")
        return self.cleaned_data

class SearchForm(forms.Form):
    searchDetail=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':"Item(i.e. SchoolBag) or Profile(i.e. BUET) ...", 'required data-validation-required-message':'Cannot search blank query.'}),
        required=True,
        )
    def __init__(self, *args, **kwargs):

        instance = kwargs.get('instance', None)

        kwargs.update(initial={
            # 'field': 'value'
        })

        super(SearchForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(SearchForm, self).clean()
        return self.cleaned_data



class MoneyBag(forms.Form):
    status=forms.BooleanField(
        required=False,
    )
    postername=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Name*','required data-validation-required-message':'Please enter Your Name.'}),
        max_length=40,
        required=True,
        )
    mobilenumber=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Contact Number*', 'required data-validation-required-message':'Please enter a valid Mobile Number'}),
        min_length=11,
        max_length=11,
        required=True,
        )
    mailid=forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Your E-mail'}),
        required=False,
        max_length=75,
        )
    location=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Location of Incident*','required data-validation-required-message':'Please enter where you lost/found it.'}),
        max_length=100,
        required=True,
        )
    color=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Color of moneybag','required data-validation-required-message':'Please enter where you lost/found it.'}),
        max_length=100,
        required=False,
        )
    def __init__(self, *args, **kwargs):

        instance = kwargs.get('instance', None)

        kwargs.update(initial={
            # 'field': 'value'
        })

        super(MoneyBag, self).__init__(*args, **kwargs)

    def clean(self):
        super(MoneyBag, self).clean()
        return self.cleaned_data






class DetailedPost(forms.Form):
    status=forms.BooleanField(
        required=False,
    )
    postername=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Name*','required data-validation-required-message':'Please enter Your Name.'}),
        max_length=40,
        required=True,
        )
    mobilenumber=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Contact Number*', 'required data-validation-required-message':'Please enter a valid Mobile Number'}),
        min_length=11,
        max_length=11,
        required=True,
        )
    mailid=forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Your E-mail'}),
        required=False,
        max_length=75,
        )
    definition=forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','rows':'8','placeholder':'Description of the Object*','required data-validation-required-message':'Please describe the Object that you lost/found.'}),
        required=True,
        max_length=300,
    )
    description=forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','rows':'8','placeholder':'Description of the corresponding Incident*','required data-validation-required-message':'Please briefly describe how you lost/found it.'}),
        required=True,
        max_length=600,
    )
    location=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id':'locationSearchField', 'placeholder':'Location of Incident*','required data-validation-required-message':'Please enter where you lost/found it.'}),
        max_length=100,
        required=True,
        )

    fdate=forms.DateField(
        #initial=date.today(),
        widget=forms.DateInput(attrs={'id':'idate','placeholder':'Date of Incident', 'class':'form-control','type':'text','onfocus':"(this.type='date')"}),
        required=False,
        )
    time=forms.TimeField(
        #initial=datetime.now(),
        widget=forms.TimeInput(attrs={'placeholder':'Time of Incident', 'class':'form-control','type':'text','onfocus':"(this.type='time')"}),
        )
    image=forms.ImageField(
        widget=forms.FileInput(attrs={'placeholder':'Visual of the Object', 'class':'form-control','multiple':'true','type':'text','onfocus':"(this.type='file')"}),
        required=False,
        )



    def __init__(self, *args, **kwargs):

        instance = kwargs.get('instance', None)

        kwargs.update(initial={
            # 'field': 'value'
        })

        super(DetailedPost, self).__init__(*args, **kwargs)

    def clean(self):
        super(DetailedPost, self).clean()
        return self.cleaned_data
