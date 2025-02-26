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

        # Validate if the date firld is empty
        if date is None:
            raise ValidationError("Please provide a valid booking date.")

        # Prevent booking dates in the past
        if date < timezone.now().date():
            raise ValidationError("Booking date cannot be in the past.")

        return date
