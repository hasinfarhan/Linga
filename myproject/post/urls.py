from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^(?P<postId>\d+)$',views.index,name='index'),

    ]
