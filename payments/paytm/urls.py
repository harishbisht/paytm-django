from django.urls import re_path
from paytm.views import home, payment, response

urlpatterns = [

    re_path(r'^$', home, name='home'),
    re_path(r'^payment/', payment, name='payment'),
    re_path(r'^response/', response, name='response'),
]
