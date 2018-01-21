from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Primary Address'}),
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
        password1 = self.cleaned_data.get('password1')
        confirmPassword = self.cleaned_data.get('confirmPassword')
        if password1 and password1 != confirmPassword:
            self._errors['password1'] = self.error_class(
                ['Passwords don\'t match'])
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

    date=forms.DateField(
        widget=forms.DateInput(attrs={'placeholder':'Date of Incident', 'class':'form-control','type':'text','required data-validation-required-message':'Please enter when you lost/found it.', 'onfocus':"(this.type='date')"}),
        )
    time=forms.TimeField(
        widget=forms.TimeInput(attrs={'placeholder':'Time of Incident', 'class':'form-control','type':'text', 'required data-validation-required-message':'Please enter when you lost/found it.','onfocus':"(this.type='time')"}),
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
