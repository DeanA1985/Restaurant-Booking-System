from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from restaurant_booking.forms import BookingForm
from accounts.models import Booking

# Restrict Access to Bookings


@login_required
def view_bookings(request):
    if request.user.is_staff:
        # Admin (staff) can see all bookings
        bookings = Booking.objects.all()
    else:
        # customers (not admin) can only see their own bookings
        bookings = Booking.objects.filter(user=request.user)

    return render(
        request,
        "bookings/booking_list.html",
        {"bookings": bookings}
    )

# Create a new booking


@login_required
def create_booking(request):
    """Handles booking creation form submission."""
    if request.method == "POST":
        form = BookingForm(request.POST)  # Get data from form
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()  # Saves to database
            return redirect("view_bookings")
        else:
            print("Form errors:", form.errors)  # prints errors
    else:
        form = BookingForm()

    return render(request, "bookings/booking_form.html", {"form": form})
