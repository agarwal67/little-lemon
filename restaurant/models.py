from django.db import models
from datetime import datetime

# Create your models here.
class Booking(models.Model):
    ID = models.DecimalField(max_digits=11, decimal_places=0, primary_key=True)
    Name = models.CharField(max_length=255, blank=False)
    No_of_guests = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    BookingDate = models.DateTimeField(default=datetime.now)

class Menu(models.Model):
    ID = models.DecimalField(max_digits=5, decimal_places=0, primary_key=True)
    Title = models.CharField(max_length=255, blank=False)
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Inventory = models.DecimalField(max_digits=5, decimal_places=0, default=0)
