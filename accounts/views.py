"""
This module contains all the view functions for user
Registration, Booking Creation, and authentication-
related features in the restaurant booking system.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from restaurant_booking.forms import BookingForm

#  User Registration View


def register(request):
    """
    Handles user registration using Django's built in User
    Creation form. Logs user in after successful
    registration.
    """
    if request.method == "POST":  # If form is submitted
        form = UserCreationForm(request.POST)  # Djangos built in reg form
        if form.is_valid():
            user = form.save()  # Saves a new user
            login(request, user)  # Logs in the user
            return redirect('home')  # Redirects to home page
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

# Forgot Password View


def forgot_password(request):
    """
    Custom forgot password view that checks if a user with
    the given email exists. If found, displays a success
    message; otherwise, shows an error message.
    """
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            User.objects.get(email=email)
            messages.success(
                request,
                "A password reset link has been sent to your email."
            )
        except User.DoesNotExist:
            messages.error(request, "No account found with that email.")
        return redirect('forgot_password')

    return render(request, "forgot_password.html")


#  Home Page View


def home(request):
    return render(request, "home.html")  # Loads home html

# Booking Creation View


@login_required  # Ensure only logged-in users can make bookings
def create_booking(request):
    """Handles booking form submission"""
    if request.method == "POST":
        form = BookingForm(request.POST)  # Capture form data
        if form.is_valid():  # Validate input
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('view_bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', )
