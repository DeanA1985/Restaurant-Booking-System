from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the default Django User Model


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Link booking to a user
    table_number = models.PositiveIntegerField(
        help_text="Ensures table numbers are positive"
    )
    date = models.DateField()  # Date of Booking
    time = models.TimeField()  # Time of Booking
    guests = models.PositiveIntegerField(
        help_text="Number of guests"
    )

    class Meta:
        ordering = ['date', 'time']  # Order by date and time

        def __str__(self):
            return (
                f"Booking by {self.user.username} "
                f"on {self.date} at {self.time}"
            )
