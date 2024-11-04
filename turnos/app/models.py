from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')

class Appointment(models.Model):
    appointment_type = models.CharField(max_length=100)
    duration = models.DurationField()
    availability = models.DateTimeField()
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'})

class Booking(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'client'})
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    booking_date = models.DateTimeField(auto_now_add=True)

