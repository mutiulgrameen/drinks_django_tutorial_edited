from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
#from django.conf.urls import url
from . import views
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
#from django.conf.urls import url
from . import views

urlpatterns= [
#    path('', views.my_view, name='my_view')
#    path('', views.Youtube.as_view())
#    path('', views.ASHABot1.as_view())
    path('', views.Welcome, name='Welcome'),
#    path('chat', views.Chat1, name = 'chat'),
]