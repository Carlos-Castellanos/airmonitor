from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Measurements(models.Model):
    name = models.CharField(max_length=10)
    measurementDate =  models.DateField(default=datetime.now, blank=True)
    measurementTime =  models.TimeField(default=datetime.now, blank=True)
    Latitude = models.DecimalField(default=0, max_digits=8, decimal_places=5)
    Longitude =  models.DecimalField(default=0, max_digits=8, decimal_places=5)
    Temperature =   models.DecimalField(default=0, max_digits=6, decimal_places=2)
    Humidity =   models.DecimalField(default=0, max_digits=6, decimal_places=2)
    Pression =   models.DecimalField(default=0, max_digits=6, decimal_places=2)
    PM25 =   models.DecimalField(default=0, max_digits=6, decimal_places=2)
    PM10 =  models.DecimalField(default=0, max_digits=6, decimal_places=2)
    id = models.AutoField(primary_key=True)
    # sensor = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE
    # )
    class Meta:
        verbose_name = 'Measurement'
        verbose_name_plural = 'measurements'
        ordering = ['id']
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):  ## is executed when a form is used, resolves the error after the POST
        return reverse("pages/home")
