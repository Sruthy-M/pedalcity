from django.contrib import admin
from web import models


class DisplayBooking(admin.ModelAdmin):
    list_display = ['name', 'phone', 'location_from', 'location_to', 'pickup_time']

admin.site.register(models.Booking, DisplayBooking)
