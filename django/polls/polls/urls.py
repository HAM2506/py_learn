from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^poll_app/', include('poll_app.urls')),
    url(r'^admin/', admin.site.urls),
]