from django.urls import path
from .views import *

urlpatterns = [
    path('indexes/', index),
    path('base/', base),
    path('csrf1/', csrf1),
    path('csrf2/', csrf2),
    path('verifyCode/', verifyCode),
]