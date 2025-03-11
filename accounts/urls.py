"""
URL configuration for the accounts app.
This file incldues route definitions for user registration,
login, logout, and custom password reset functionality.
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='home'),
        name='logout'
    ),
    path(
        'register/',
        views.register,
        name='register'
    ),
    path(
        'forgot-password/',
        views.forgot_password,
        name='forgot_password'
    ),
]
