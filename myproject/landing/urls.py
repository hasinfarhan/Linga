from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^detpro$',views.detailedProfile,name='detailedProfile'),
    url(r'^register$',views.registerUser,name='reguser'),
    url(r'^login$',views.loginUser,name='loginuser'),
    url(r'^logout$',views.logoutUser,name='logoutuser'),
    url(r'^postfeed$',views.createPost,name='createpost'),
    url(r'^searchTokenize$',views.doSearch,name='doSearch'),
    url(r'^postfeed_moneybag$',views.createmoneybagPost,name='createmoneybag')
    ]
