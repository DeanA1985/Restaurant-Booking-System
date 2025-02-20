from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def home(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return render(request, "logout_confirm.html")
