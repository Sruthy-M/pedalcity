from django.db import models
from django.db.models.fields import EmailField


# grab a pedal
class Booking(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    location_from = models.CharField(max_length=200)
    location_to = models.CharField(max_length=200)
    pickup_time = models.TimeField()

    def __str__(self):
        return self.name