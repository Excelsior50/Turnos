from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return self.username


class Appointment(models.Model):
    appointment_type = models.CharField(max_length=100)
    duration = models.DurationField(help_text="Duration of the appointment")
    availability = models.DateTimeField(help_text="Date and time this appointment is available")
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'})

    def __str__(self):
        return f"{self.appointment_type} - {self.availability}"

class Booking(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'client'})
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.client.username} for {self.appointment}"

