from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^get_topic/$', views.get_topic, name='get_topic'),
    url(r'^save_topic/$', views.save_topic, name='save_topic')
]