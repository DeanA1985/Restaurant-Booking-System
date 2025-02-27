from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Booking(models.Model):
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

    def clean(self):
        """ Custom validation to prevent past bookings and double bookings"""
        if not self.date:
            raise ValidationError("Date is required.")

        if self.date < timezone.now().date():
            raise ValidationError("Booking date cannot be in the past.")

        # Prevent double bookngs for the same table,date and time
        is_booked = Booking.objects.filter(
            table_number=self.table_number,
            date=self.date,
            time=self.time
        ).exists()

        if is_booked:
            raise ValidationError(
                f"Table {self.table_number} is already booked at this time."
            )

        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Booking for {self.guests} guests on {self.date} "
            f"at {self.time} (Table {self.table_number})"
        )
