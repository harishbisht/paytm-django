from django.urls import re_path
from paytm.views import home, payment, response

urlpatterns = [

    re_path(r'^$', home, name='home'),
    re_path(r'^payment/', payment, name='payment'),
    # REPLACE USERNAME WITH PRIMARY KEY OF YOUR USER MODEL
    re_path(r'^response/(?P<user_id>\w+)/$', response, name='response'),
]
