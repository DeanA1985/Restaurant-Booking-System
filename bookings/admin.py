from django.contrib import admin
from .models import Table, Booking  # Import the models

# Register Table model
admin.site.register(Table)

# Register Booking model
admin.site.register(Booking)
