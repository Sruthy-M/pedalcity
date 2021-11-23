from django.shortcuts import render
from django.http import HttpResponseRedirect
from web.forms import *
from web.models import Booking


def home_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form = BookingForm()
    context = {
        'form':form,
        }
    return render(request, 'web/index.html', context)


def booking_detail(request):
    bookings = Booking.objects.all().order_by('-pickup_time')
    context = {
        'bookings': bookings
    }
    return render(request, 'web/booking_details.html', context)