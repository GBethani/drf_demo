from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
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

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def createToken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)