from urllib import request
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import( 
    CreateView, 
    DeleteView,
    UpdateView
)


from django.shortcuts import render, redirect, get_object_or_404


# https://docs.djangoproject.com/en/4.1/ref/class-based-views/flattened-index/
from django.urls import is_valid_path, reverse_lazy
from .models import Sensor

# Create your views here.

class SensorListView(ListView):
    template_name = "sensors/list.html"   
    model = Sensor


class SensorDetailView(DetailView):
    template_name = "sensors/detail.html"  
    model = Sensor

class SensorCreateView(CreateView): #113
    template_name = "sensors/new.html"  
    model = Sensor
    fields = ["name","Latitude","Longitude","Temperature","Humidity","Pression","PM25","PM10"]  

    # def form_valid(self, form):       #take tha user and save it like author'field
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


class SensorUpdateView(UpdateView): #113
    template_name = "sensors/edit.html"  
    model = Sensor
    fields = ["name","Latitude","Longitude","Temperature","Humidity","Pression","PM25","PM10"]   

    def test_func(self):                                #113
        obj = self.get_object()
        return obj.author == self.request.user


class SensorDeleteView(DeleteView):  #113
    template_name = "sensors/delete.html"  
    model = Sensor
    success_url = reverse_lazy('sensor_list')

    def test_func(self):                                #113
        obj = self.get_object()
        return obj.author == self.request.user