from django.urls import path
from .views import ReservationListView, ReservationUpdateView, ReservationDeleteView,ReservationLiberateView,  TimeSlotListCreateAPIView , ReservationDetailView,  ReservationCreateView,ReservationMoveAPIView,ReservationReleaseAPIView

urlpatterns = [
    #path('reservations/', ReservationListView.as_view(), name='reservation-list'),
    path('reservations/create/', ReservationCreateView.as_view(), name='reservation-create'),
    path('reservations/<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation-update'),
    path('reservations/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation-delete'),
    path('reservations/<int:pk>/liberate/', ReservationLiberateView.as_view(), name='reservation-liberate'),
    #path('reservations/<int:pk>/move/',  ReservationMoveView.as_view(), name='reservation-move'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),

    path('reservations/move/<int:pk>/', ReservationMoveAPIView.as_view(), name='reservation-move'),
    path('reservations/release/<int:pk>/', ReservationReleaseAPIView.as_view(), name='reservation-release'),
    path('time-slots/', TimeSlotListCreateAPIView.as_view(), name='time-slot-list-create'),
    path('reservations/', ReservationListView.as_view(), name='reservation-list'),
    #path('reservations/create/', ReservationListView.as_view(), name='reservation-create'),
]
