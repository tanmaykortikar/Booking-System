# booking/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity_available = models.PositiveIntegerField()

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    quantity_booked = models.PositiveIntegerField(default=1)