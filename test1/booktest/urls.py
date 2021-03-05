from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'indexes/', index),
    url(r'^(?P<p2>\d+)/(?P<p1>\d+)/(?P<p3>\d+)/$', detail),
    url('test1/', test1),
    url('test2', test1),
    # url(r'^test2/$', test2),
    # url(r'^(\d+)/(\d+)/(\d+)/$', detail),
    url('cookie_set',cookie_set),
    url('redTest', redTest),


    url('session1/', session1),
    url('session2/', session2),
    url('session3/', session3),
    url('session2_handle/', session2_handle),
]