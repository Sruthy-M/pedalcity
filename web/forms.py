from django import forms
from web import models


class BookingForm(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = '__all__'