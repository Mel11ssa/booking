
"""
from django.db import models

class Reservation(models.Model):
    conteneur = models.CharField(max_length=50)
    reference_transport = models.CharField(max_length=50)
    terminal = models.CharField(max_length=50, default='teract-best')
    date = models.DateField()
    status = models.CharField(max_length=50, choices=[('reserve', 'Réservé'), ('libre', 'Libre')])
"""

from django.db import models
from django.contrib.auth.models import User
"""
class Reservation(models.Model):
    TERMINAL_CHOICES = [
        ('teract-best', 'TERACT-BEST'),
        ('teract-bej', 'TERACT-BEJ'),
        
    ]

    STATUS_CHOICES = [
        ('reserve', 'Réservé'),
        ('libre', 'Libre'),
    ]

    terminal = models.CharField(max_length=255)
    container = models.CharField(max_length=255, null=True, blank=True)
    operation = models.CharField(max_length=255,null= True, blank=True)
    status = models.CharField(max_length=50)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=  True)

    def __str__(self):
        return f"{self.container} - {self.status} - {self.date}"
"""

from django.db import models
from django.contrib.auth.models import User




class TimeSlot(models.Model):
    terminal = models.CharField(max_length=50,default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.IntegerField(default=0)
    reservations = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.terminal} - {self.start_time} to {self.end_time} (Capacity: {self.capacity}, Reservations: {self.reservations})"

    def is_available(self):
        return self.reservations < self.capacity

class Reservation(models.Model):
    TERMINAL_CHOICES = [
        ('teract-best', 'TERACT-BEST'),
        ('teract-bej', 'TERACT-BEJ'),
        
    ]
    STATUS_CHOICES = [
        ('reserve', 'Réservé'),
        ('libre', 'Libre'),
    ]

    container = models.CharField(max_length=255, null=True, blank=True)
   
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.container} - {self.status} - {self.date}"



