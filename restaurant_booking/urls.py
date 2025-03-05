"""
URL configuration for restaurant_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import home
from .views import (
    view_bookings,
    create_booking,
    modify_booking,
    cancel_booking
)  # Import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # Include authentication system
    path('accounts/', include("accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),

    #  Booking URLS
    path(
        'bookings/',
        view_bookings,
        name="view_bookings"
    ),
    path(
        'bookings/new/',
        create_booking,
        name="create_booking"
    ),
    path(
        'bookings/<int:booking_id>/modify/',
        modify_booking,
        name="modify_booking"
    ),
    path(
        'bookings/<int:booking_id>/cancel/',
        cancel_booking,
        name="cancel_booking"
    ),
]
