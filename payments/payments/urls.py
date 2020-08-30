from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path
from paytm.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', home, name='home'),
    re_path(r'^paytm/', include('paytm.urls')),
    re_path(r'^accounts/', include('allauth.urls')),
]
