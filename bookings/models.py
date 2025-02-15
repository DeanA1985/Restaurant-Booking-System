# Import Django's built-in models
from django.db import models

# Import Django's built-in User model (used for authentication)
from django.contrib.auth.models import User


# =======================================
# Table Model (Represents restaurant tables)
# =======================================
class Table(models.Model):
    number = models.IntegerField(unique=True)  # Each table has a unique number
    capacity = models.IntegerField()  # Number of seats available at each table

    def __str__(self):
        return f"Table {self.number} (Seats {self.capacity})"

# ========================================
# Booking Model (Represents reservations)
# ========================================


class Booking(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE
    )   # Links a booking to a user. If the user is deleted the booking is too
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE
    )   # Links a table to a user. If the table is deleted, its bookings also
    date = models.DateField()   # The date of the reservation
    time = models.TimeField()   # The time of the reservation
    guests = models.IntegerField()   # Number of guests that are included

    def __str__(self):
        # Displays booking info in specific format below
        return (
            f"Booking by {self.customer.username} "
            f"for {self.guests} guests on {self.date} at {self.time}"
        )
