from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=10)
    Latitude= models.BooleanField()
    Longitude= models.BooleanField()
    Temperature= models.BooleanField()
    Humidity= models.BooleanField()
    Pression= models.BooleanField()
    Altitud= models.BooleanField()
    PM10= models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):  ## is executed when a form is used, resolves the error after the POST
        return reverse("sensor_list")

        #return reverse("pages/home")