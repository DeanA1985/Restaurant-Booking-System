from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


from .forms import BookingForm
from accounts.models import Booking


# ==============================
# Restrict Access to Bookings
# ==============================


@login_required
def view_bookings(request):
    """ View a list of bookings"""
    if request.user.is_staff:
        # Admin (staff) can see all bookings
        bookings = Booking.objects.all()
    else:
        # Customers (not admin) can only see their own bookings
        bookings = Booking.objects.filter(user=request.user)

    for booking in bookings:
        # Debugging output to verify in terminal
        print(
            f"Booking ID: {booking.id}, "
            f"Date: {booking.date}, "
            f"Time: {booking.time}, "

        )

    return render(
        request,
        "bookings/booking_list.html",
        {"bookings": bookings}
    )
# =======================================
# Create a new booking with validation
# =======================================


@login_required
def create_booking(request):
    """Handles booking creation form submission."""
    available_times = [
        "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
        "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
        "15:00", "15:30", "16:00", "16:30", "17:00", "17:30",
        "18:00", "18:30", "19:00", "19:30", "20:00", "20:30",
    ]

    if request.method == "POST":
        form = BookingForm(request.POST)  # Get data from form
        if form.is_valid():
            try:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.clean()
                booking.save()  # Saves to database
                messages.success(request, "Booking created successfully!")
                return redirect("view_bookings")
            except ValidationError as e:
                form.add_error(None, e.message)
                messages.error(request, str(e))
    else:
        form = BookingForm()

    return render(request, "bookings/booking_form.html", {
        "form": form,
        "available_times": available_times
    })

# ======================================
# Cancel a booking
# ======================================


@login_required
def cancel_booking(request, booking_id):
    try:
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        booking.delete()
        messages.success(request, "Booking cancelled successfully!")
    except Booking.DoesNotExist:
        messages.error(request, "Booking not found.")
    return redirect("view_bookings")

# ==========================================
# Modify a Booking
# ==========================================


@login_required
def modify_booking(request, booking_id):
    """Allows a user to modify and existing booking"""
    try:
        booking = Booking.objects.get(id=booking_id, user=request.user)
    except Booking.DoesNotExist:
        messages.error(request, "Booking not found.")
        return redirect("view_bookings")

    available_times = [
        "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
        "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
        "15:00", "15:30", "16:00", "16:30", "17:00", "17:30",
        "18:00", "18:30", "19:00", "19:30", "20:00", "20:30",
    ]

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            try:
                updated_booking = form.save(commit=False)
                updated_booking.clean()
                updated_booking.save()
                messages.success(request, "Booking modified successfully!")
                return redirect("view_bookings")
            except ValidationError as e:
                form.add_error(None, e)  # Show validation errors

    else:
        form = BookingForm(instance=booking)
        form.fields['date'].initial = booking.date.strftime('%Y-%m-%d')
        form.fields['time'].initial = booking.time.strftime('%H:%M')

        return render(request, "bookings/modify_booking.html", {
            "form": form,
            "booking": booking,
            "available_times": available_times

        })
