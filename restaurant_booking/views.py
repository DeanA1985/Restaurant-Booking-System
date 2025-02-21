from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
