from django.conf.urls import url
from basic_app import views

from django.urls import path


app_name='basic_app'


urlpatterns=[
path(r'relative/',views.relative,name='relative'),
path(r'other/',views.others,name='others'),



]
