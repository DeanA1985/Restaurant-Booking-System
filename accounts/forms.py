from django import forms  # Djangos built in form system
from .models import Booking  # Import the booking model

#  Define a form that lets users input booking details


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking  # Link this form to the Booking model
        fields = ['table_number', 'date', 'time', 'guests']
