from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class DataSensor(models.Model):

sensorID
    measurementDateTime =  models.DateTimeField()
    Latitude = models.DecimalField(..., max_digits=18, decimal_places=15)
    Longitude = models.DecimalField(..., max_digits=18, decimal_places=15)
    Temperature =  models.DecimalField(..., max_digits=6, decimal_places=2)
    Humidity =  models.DecimalField(..., max_digits=6, decimal_places=2)
    Pression =  models.DecimalField(..., max_digits=6, decimal_places=2)
    Altitud =  models.DecimalField(..., max_digits=6, decimal_places=2)
    PM10 =  models.DecimalField(..., max_digits=6, decimal_places=2)
    sensor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):  ## is executed when a form is used, resolves the error after the POST
        return reverse("post_list")

        #return reverse("pages/home")
