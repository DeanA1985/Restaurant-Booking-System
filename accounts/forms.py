"""
This module defines the forms used in the restaurant booking
system. Includes custom validation for booking dates and
fields.
"""
from django import forms  # Djangos built in form system
from accounts.models import Booking  # Import the booking model
from datetime import datetime, time, timedelta


def generate_time_choices():
    start_time = time(9, 0)
    end_time = time(18, 30)
    interval = timedelta(minutes=30)

    times = []
    current_datetime = datetime.combine(datetime.today(), start_time)

    while current_datetime.time() <= end_time:
        time_str = current_datetime.strftime('%H:%M')
        times.append((time_str, time_str))
        current_datetime += interval

    return times


class BookingForm(forms.ModelForm):
    """ Booking form for table reservation """


table_number = forms.IntegerField(
         widget=forms.NumberInput(attrs={'placeholder': '1-20'}),
         min_value=1, max_value=20
    )

date = forms.DateField(
         widget=forms.DateInout(attrs={'type': 'date'})
    )

time_slot = forms.ChoiceField(
         choices=generate_time_choices(),
         widget=forms.Select()
    )

guests = forms.IntegerField(
         min_value=1, max_value=10,
         widget=forms.NumberInput(attrs={'placeholder': '1-10'})
    )


class Meta:
    model = Booking  # Link this form to the Booking model
    fields = ['table_number', 'date', 'time', 'guests']
