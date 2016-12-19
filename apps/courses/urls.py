from django.conf.urls import url
from views import index, new, create, add_student_page
from views import add_student_to_course, show, destroy

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^new/$', new, name="new"),
    url(r'^create/$', create, name="create"),
    url(r'^add_student_page/$', add_student_page, name="add_student_page"),
    url(r'^add_student_to_course/$', add_student_to_course, name="add_student_to_course"),
    url(r'^show/(?P<course_id>\d+)/$', show, name="show"),
    url(r'^destroy/$', destroy, name="destroy")
]
