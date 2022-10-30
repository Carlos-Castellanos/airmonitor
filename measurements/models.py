from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from sensors.models import Sensor

# Create your models here.
class Measurements(models.Model):
    idSensor = models.IntegerField(null=False)
    measurementDate =  models.DateField(default=datetime.now, blank=True)
    measurementTime =  models.TimeField(default=datetime.now, blank=True)
    Latitude = models.DecimalField(default=0, max_digits=10, decimal_places=7)
    Longitude =  models.DecimalField(default=0, max_digits=10, decimal_places=7)
    Temperature =   models.DecimalField(default=0, max_digits=6, decimal_places=2)
    Humidity =   models.DecimalField(default=0, max_digits=6, decimal_places=2)
    Pression =   models.DecimalField(default=0, max_digits=6, decimal_places=2)
    PM25 =   models.DecimalField(default=0, max_digits=6, decimal_places=2)
    PM10 =  models.DecimalField(default=0, max_digits=6, decimal_places=2)
    id = models.AutoField(primary_key=True)
    
    idSensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT, null=True)

    class Meta:
        verbose_name = 'Measurement'
        verbose_name_plural = 'measurements'
        ordering = ['measurementDate','measurementTime','idSensor']
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):  ## is executed when a form is used, resolves the error after the POST
        return reverse("pages/home")
