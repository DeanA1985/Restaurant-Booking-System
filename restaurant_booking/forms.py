from django import forms
from accounts.models import Booking  # Imports the Booking Model
from django.utils import timezone


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table_number', 'date', 'time', 'guests']  # fields


def clean_date(self):
    date = self.cleaned_data.get("date")
    print("Checking date validation.")
    if date and date < timezone.now().date():  # Checks if the date is before
        print("Error: Date is in the past!")
        raise forms.ValidationError("Booking date cannot be in the past")
    return date


def clean_table_number(self):
    table_number = self.cleaned_data.get('table_number')
    if table_number < 1 or table_number > 20:  # Restricts table numbers
        raise forms.ValidationError("Table number must be between 1 and 20.")
    return table_number


def clean_guests(self):
    guests = self.cleaned_data.get('guests')
    if guests > 10:  # Restricts guest count
        raise forms.ValidationError(
            "A maximum of 10 guests per booking is allowed."
        )
    return guests
