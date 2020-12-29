from rest_framework import serializers
from .models import Flight, Passenger, Reservation
import re

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flightnumber(self,flightnumber):
        if(re.match("^[a-zA-Z0-9]*$",flightnumber)==None):
            raise serializers.ValidationError("Only AlphaNumerics are allowed")
        return flightnumber

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'