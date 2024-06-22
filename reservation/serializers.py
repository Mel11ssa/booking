# serializers.py
from rest_framework import serializers
from .models import Reservation
"""
class ReservationSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Reservation.STATUS_CHOICES)
    #terminal = serializers.ChoiceField(choices=Reservation.TERMINAL_CHOICES)
    class Meta:
        model = Reservation
        fields = ['terminal', 'container',  'status', 'date', 'user']
"""

from rest_framework import serializers
from .models import  Reservation , TimeSlot
class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'container', 'status', 'date', 'user', 'time_slot']
