
from django.shortcuts import render, redirect
# So we can count the students in a class
from django.db.models import Count
from ..courses.models import Course
from ..users.models import User
# Create your views here.
def index(request):
    context = {
        'users' : User.objects.all(),
        'courses' : Course.objects.annotate(students=Count('users')),
    }
    return render(request, 'courses_and_users_app/index.html', context)

def create(request):
    Course.objects.add_user_to_course(request.POST)
    return redirect("courses_and_users:courses_users_index")
