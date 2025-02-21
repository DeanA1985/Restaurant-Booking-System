from django import forms
from accounts.models import Booking  # Imports the Booking Model


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table_number', 'date', 'time', 'guests']  # fields
