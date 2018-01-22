from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^profiles/(?P<tokenHash>\w+)$',views.profiles,name='profiles'),
    url(r'^posts/(?P<tokenHash>\w+)$',views.index,name='index'),
    ]
