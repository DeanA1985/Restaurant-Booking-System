from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

# Register User


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = RegisterForm()
            return render(request, "accounts/register.html", {"form": form})

# Login User


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request, "accounts/login.html", {"form": form})

# Logout User


def user_logout(request):
    logout(request)
    return redirect('login')
