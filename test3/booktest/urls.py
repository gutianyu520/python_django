from django.urls import path

from .views import *

urlpatterns = [
    path('indexes/', index),
    path('myex/', myex),
    path('uplao/', uplao),
    path('upload/', upload),
    path('pageList/<int:indexes>/', pageList),
    path('pageList/', pageList),
    path('region/', region),
    path('htmlEditor/', htmlEditor),
    path('cache1/', cache1),
    path('mysearch/', mysearch),
    path('celery_common/', celery_common),
    path('celery_delay/', celery_delay),
    path('region_select/<int:pid>', region_select),
]