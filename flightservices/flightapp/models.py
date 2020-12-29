from django.db import models

# Create your models here.
class Flight(models.Model):
    flightnumber = models.CharField(max_length=10)
    operatingairlines = models.CharField(max_length=10)
    departurecity = models.CharField(max_length=10)
    arrivalcity = models.CharField(max_length=10)
    dateofdeparture = models.DateField()
    estimatedtimeofdeparture = models.TimeField()

    def __str__(self):
        return self.departurecity + '-' + self.arrivalcity

class Passenger(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.email

class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)

    def __str__(self):
        return self.flight + ' by '+ self.passenger