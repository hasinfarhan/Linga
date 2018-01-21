from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^(?P<tokenHash>\w+)$',views.index,name='index'),


    ]
