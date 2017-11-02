from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^get_hello/$', views.get_hello, name='get_hello'),
    url(r'^get_helloCount/$', views.get_helloCount, name='get_helloCount'),
]