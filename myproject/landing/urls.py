from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^register_as_user$',views.registerUser,name='reguser'),
    url(r'^register_as_page$',views.registerPage,name='regpage'),
    url(r'^postfeed$',views.createPost,name='createpost')

    ]
