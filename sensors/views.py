from urllib import request
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import( 
    CreateView, 
    DeleteView,
    UpdateView
)
import folium
from .data import *

from django.shortcuts import render, redirect, get_object_or_404


# https://docs.djangoproject.com/en/4.1/ref/class-based-views/flattened-index/
from django.urls import is_valid_path, reverse_lazy

from measurements.models import Measurements
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
    fields = ["idSensor","name","Latitude","Longitude","Temperature","Humidity","Pression","PM25","PM10"]  

    # def form_valid(self, form):       #take tha user and save it like author'field
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


class SensorUpdateView(UpdateView): #113
    template_name = "sensors/edit.html"  
    model = Sensor
    fields = ["idSensor","name","Latitude","Longitude","Temperature","Humidity","Pression","PM25","PM10"]   

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
    
class FoliumView(TemplateView):
    template_name = "sensors/sensor_map.html"
    model = Sensor
    #form_class = RevisionForm 

    def get_context_data(self, **kwargs):

        for key, value in kwargs.items():
            print("{0} = {1}".format(key, value))
        print(kwargs["yy"])
        datas = datasYY(2021)
        m = folium.Map(
            location=[32.6207486, -115.3982056],
            zoom_start=13
            ) 
        
        sensores = Sensor.objects.all()
        print("dictionarySensor")
        for a in sensores:
            print(datas['idSensor'][a.idSensor])

        for a in sensores:
            folium.Marker(
                location=[a.Latitude, a.Longitude],
                tooltip="Click for information",
                popup=folium.Popup(f"""Sensor= {a.name} <br>
                       Temp = {datas['Temp'][a.idSensor]:,.2f} °C<br>
                       Hum = {datas['Hum'][a.idSensor]:,.2f} %<br>
                       Pres = {datas['Pres'][a.idSensor]:,.2f} kPa<br>
                       pm 2.5 = {datas['PM25_x'][a.idSensor]:,.4f} µg/m<sup>3</sup><br>
                       pm 10 = {datas['PM10_x'][a.idSensor]:,.4f} µg/m<sup>3</sup><br>
                    """, max_width=len(f"name= {a.name}")*20),
                icon=folium.Icon(icon='cloud')
            ).add_to(m)

        
        m = m._repr_html_()
        return {"m": m}
    
 


 
    
    
    
    