from django.conf.urls import url
from views import login_page, register, login, logoff

urlpatterns = [
    url(r'^$', login_page, name='login_page'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logoff/$', logoff, name='logoff')
]
