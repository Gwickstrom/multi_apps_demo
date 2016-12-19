from django.conf.urls import url
from views import index, create
urlpatterns = [
    url(r'^$', index, name='courses_users_index'),
    url(r'^usercourse$', create, name='courses_users_create'),
]
