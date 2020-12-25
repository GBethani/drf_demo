from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    features = models.CharField(max_length=100)
    loves = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return str(self.id)