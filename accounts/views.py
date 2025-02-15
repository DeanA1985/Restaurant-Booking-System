from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# =============================================
# Register New Users
# =============================================


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')   # Redirect to homepage after registering
        else:
            form = UserCreationForm()
            return render(request, 'accounts/register.html', {'form': form})

# =============================================
# Log In Existing Users
# =============================================


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request, 'accounts/register.html', {'form': form})

# =============================================
# Log Out Users
# =============================================


def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page
