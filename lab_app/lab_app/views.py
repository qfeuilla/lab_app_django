from os import error
from django.contrib.auth import forms
from django.shortcuts import render, redirect
from .forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User " + form.cleaned_data.get('username') + " successfuly created")
            return redirect('login')
        else:
            for key, err in form.errors.items():
                messages.error(request, key + ": " + err[0])
            return redirect("register")

    context = {'form': form}
    return render(request, "accounts/register.html", context)

def loginPage(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "User " + user.get_username() + " successfuly login")
            return redirect('home')
        else:
            messages.info(request, "username or password incorect")

    return render(request, "accounts/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("login")

def homePage(request):
    context = {}
    return render(request, "home.html", context)