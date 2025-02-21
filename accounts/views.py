from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import BookingForm   # Import the booking form

#  User Registration View


def register(request):
    if request.method == "POST":  # If form is submitted
        form = UserCreationForm(request.POST)  # Djangos built in reg form
        if form.is_valid():
            user = form.save()  # Saves a new user
            login(request, user)  # Logs in the user
            return redirect('home')  # Redirects to home page
    else:
        form = UserCreationForm()

        return render(request, "registration/register.html", {"form": form})

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
