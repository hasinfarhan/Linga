from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^(?P<postId>\d+)$',views.index,name='index'),
    url(r'^(?P<postId>\d+)/commentfeed$',views.comment,name='comment'),
    url(r'^(?P<postId>\d+)/delete$',views.delPost,name='delete'),

    ]
