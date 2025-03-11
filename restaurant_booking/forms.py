from django import forms
from accounts.models import Booking  # Imports the Booking Model
from django.core.exceptions import ValidationError
from django.utils import timezone


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['table_number', 'date', 'time', 'guests']  # fields

    def clean_date(self):
        date = self.cleaned_data.get('date')

        # Validate if the date field is empty
        if date is None:
            raise ValidationError("Please provide a valid booking date.")

        # Prevent booking dates in the past
        today = timezone.now().date()
        if date <= today:
            raise ValidationError(
                "Bookings must be made at least one day in advance."
            )

        return date

    def clean(self):
        """Check for double bookings in the form."""
        cleaned_data = super().clean()
        table_number = cleaned_data.get("table_number")
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if table_number and date and time:
            # Checks if a booking already exists
            if Booking.objects.filter(
                table_number=table_number, date=date, time=time
            ).exists():
                raise ValidationError(
                    "This table is already book at this time."
                    "Please choose a different time slot."
                )

        return cleaned_data
