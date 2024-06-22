from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Reservation
from .serializers import ReservationSerializer
"""
class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class =ReservationSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'chauffeur'):
            serializer.save()
        elif hasattr(user, 'transporteur'):
            serializer.save()
"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Reservation
from .serializers import ReservationSerializer
from django_filters.rest_framework import DjangoFilterBackend
#from .filters import ReservationFilter
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  Reservation
from .serializers import  ReservationSerializer




class ReservationListView(APIView):
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservationCreateView(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
class ReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReservationFilter


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Reservation
from .serializers import ReservationSerializer
from .permissions import IsChauffeurOrTransporteur

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = [IsAuthenticated, IsChauffeurOrTransporteur]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
"""

class ReservationUpdateView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = [IsAuthenticated]

class ReservationDeleteView(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = [IsAuthenticated]


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

class ReservationUpdateView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def liberate(self, request, pk=None):
        reservation = self.get_object()
        reservation.status = 'liberated'
        reservation.save()
        return Response({'status': 'Reservation liberated'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def move(self, request, pk=None):
        reservation = self.get_object()
        new_date = request.data.get('new_date')
        if new_date:
            reservation.date = new_date
            reservation.save()
            return Response({'status': 'Reservation moved'}, status=status.HTTP_200_OK)
        return Response({'error': 'New date not provided'}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime
from .models import Reservation
from .serializers import ReservationSerializer
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.permissions import IsAuthenticated

class ReservationLiberateView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        reservation = self.get_object()
        reservation.status = 'libre'
        reservation.save()
        return Response({'status': 'reservation liberated'})
"""
class ReservationMoveView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        reservation = self.get_object()
        new_date = request.data.get('new_date')

        if not new_date:
            raise ValidationError({'new_date': 'New date is required.'})

        try:
            new_date = datetime.strptime(new_date, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            raise ValidationError({'new_date': 'Invalid date format. Use ISO 8601 format.'})

        if new_date < timezone.now():
            raise ValidationError({'new_date': 'The new date cannot be in the past.'})

        reservation.date = new_date
        reservation.save()

        return Response({'status': 'reservation moved'}, status=status.HTTP_200_OK)
    
"""
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
class ReservationDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Reservation, pk=pk)

    def get(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reservation = self.get_object(pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TimeSlot, Reservation
from .serializers import TimeSlotSerializer, ReservationSerializer

class TimeSlotListCreateAPIView(APIView):
    def get(self, request):
        time_slots = TimeSlot.objects.all()
        serializer = TimeSlotSerializer(time_slots, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TimeSlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservationMoveAPIView(APIView):
    def post(self, request, pk):
        try:
            reservation = Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        new_time_slot_id = request.data.get('new_time_slot_id')
        try:
            new_time_slot = TimeSlot.objects.get(id=new_time_slot_id)
        except TimeSlot.DoesNotExist:
            return Response({'error': 'New time slot not found'}, status=status.HTTP_404_NOT_FOUND)

        if new_time_slot.is_available():
            # Update reservations count in the old and new time slots
            if reservation.time_slot:
                reservation.time_slot.reservations -= 1
                reservation.time_slot.save()
            new_time_slot.reservations += 1
            new_time_slot.save()

            # Update the reservation
            reservation.time_slot = new_time_slot
            reservation.save()
            return Response({'status': 'Reservation moved'}, status=status.HTTP_200_OK)
        return Response({'error': 'New time slot is not available'}, status=status.HTTP_400_BAD_REQUEST)


class ReservationReleaseAPIView(APIView):
    def post(self, request, pk):
        try:
            reservation = Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        reservation.status = 'libre'
        reservation.save()
        return Response({'status': 'Reservation released'}, status=status.HTTP_200_OK)