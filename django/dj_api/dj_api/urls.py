# coding: utf-8

from django.conf.urls import url, include
from django.contrib import admin

from test_api.urls import router as test_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #include blog.urls
    url(r'^api/', include(test_api.urls)),
]