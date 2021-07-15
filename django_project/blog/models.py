from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms


class add_flight(models.Model):
    source = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    check_in_date = models.DateTimeField(default=timezone.now)
    check_out_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(default='Admin', max_length=10)
    no_of_tickets = models.DecimalField(default=100, max_digits=3, decimal_places=0)
    class_avaiable = models.DecimalField(default=3, max_digits=1, decimal_places=0)
    radio = forms

    def __str__(self):
        return self.source


# class Booking(models.Model):
#     source = models.CharField(max_length=100)
#     To = models.CharField(max_length=100)
#     check_in_date = models.DateTimeField(default=timezone.now)
#     check_out_date = models.DateTimeField(default=timezone.now)
#     no_of_avilable_tickets = models.DecimalField(default=100, max_digits=3, decimal_places=0)
#     class_avaiable = models.DecimalField(default=3, max_digits=1, decimal_places=0)
#     no_of_booked_tickets = models.DecimalField(default=0, max_digits=2, decimal_places=0, max_value=20)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
# Create your models here.
