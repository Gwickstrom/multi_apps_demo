from django.shortcuts import render, redirect
from django.contrib import messages
# from django.db import models
from .models import User

# Create your views here.
def login_page(request):
    context = {}
    if "user_id" in request.session:
        context["user"] = User.objects.get(id=request.session["user_id"])
    return render(request, "users/login_page.html", context)

def register(request):
    #Logic goes here
    res = User.objects.register(request.POST)
    ### ADD TO SESSION ###
    if res["added"]:
        #Probably want to add to session
        messages.success(request, "Added user #{}".format(res["new_user"].id))
    else:
        for error in res['errors']:
            messages.error(request, error)

    return redirect("login_page")

def login(request):
    #error here
    user = User.objects.login(request.POST)

    if user:
        messages.success(request, "Logged in user #{}".format(user.id))
    else:
        messages.error(request, "E-mail address or password incorrect")
    #Logic goes here
    return redirect("new")

def logoff(request):
    request.session.clear()
    return redirect("login_page")
