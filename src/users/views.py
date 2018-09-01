from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout
    )
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Users

# Create your views here.
def index(request):
    user_list = Users.objects.all()
    ctx = {
        "user_list" : user_list
    }
    return render(request, "index.html", ctx)

def login(request):
    ctx = {}

    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
            # Redirect to a success page.
        else:
            ctx.update({"error" : "사용자가 없습니다."})


    return render(request, "login.html", ctx)

def signup(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        id = request.POST.get("id")
        password = request.POST.get("password")
        #password_again = request.POST.get("password_again")
        email = request.POST.get("email")
        username = request.POST.get("username")
        cellphone = request.POST.get("cellphone")

        user = User.objects.create_user(
            id, password, email, username) # cellphone)
        # print(username, email, password)

    ctx = {}
    return render(request, "signup.html", ctx)

def logout(request):
    auth_logout(request)
    return redirect("/")
