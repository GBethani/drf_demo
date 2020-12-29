from django.urls import path,include
from . views import FlightViewSet, PassengerViewSet, ReservationViewSet, find_flights,save_reservation
from rest_framework import routers

router = routers.DefaultRouter()
router.register('flights',FlightViewSet)
router.register('passenger',PassengerViewSet)
router.register('reservation',ReservationViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('find_flights/',find_flights,name = 'find-flights'),
    path('save_reservation/',save_reservation,name = 'save-reservation'),
]
