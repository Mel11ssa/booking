from django_filters import rest_framework as filters
from .models import Reservation

class ReservationFilter(filters.FilterSet):
    date_range = filters.DateFromToRangeFilter(field_name='date')

    class Meta:
        model = Reservation
        fields = {
            'terminal': ['exact', 'icontains'],
            'container': ['exact', 'icontains'],
            'operation': ['exact', 'icontains'],
            'status': ['exact', 'icontains'],
            'date': ['exact', 'gte', 'lte'],
        }
