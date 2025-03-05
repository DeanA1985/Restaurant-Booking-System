from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()


class Booking(models.Model):
    """Model for storing restaurant bookings"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    date = models.DateField()
    time = models.TimeField()

    guests = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    class Meta:
        ordering = ['date', 'time']

    @property
    def formatted_time(self):
        """Returns the time in correct format"""
        if self.time:
            return self.time.strftime("%H:%M")
        return "No Time"

    def clean(self):
        """Prevent double bookings for the same table, date and time."""
        if Booking.objects.filter(
            table_number=self.table_number,
            date=self.date,
            time=self.time
        ).exclude(pk=self.pk).exists():  # Modifications of bookings allowed
            raise ValidationError(
                "This table is already booked at this time. "
                "Please choose a different time slot."
            )

    def save(self, *args, **kwargs):
        self.clean()  # run validation before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Booking for {self.guests} guests on {self.date} "
            f"at {self.time} (Table {self.table_number})"
        )
