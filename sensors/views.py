from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import( 
    CreateView, 
    DeleteView,
    UpdateView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
   )   #113
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

class SensorCreateView(LoginRequiredMixin, UserPassesTestMixin,  CreateView):  #113
    template_name = "sensors/new.html"  
    model = Sensor
    fields = ["idSensor","name","Latitude","Longitude","Temperature","Humidity","Pression","PM25","PM10"]  
    permission_required = "sensors.change_sensor"
    
    def test_func(self):
        # print('grupos:', self.request.user.groups.all())
        # print('user:', self.request.user)
        # print(self.request.user.get_group_permissions())
        # print(self.request.user.has_perm("sensors.change_sensor")) 
        if self.request.user.has_perm("sensors.change_sensor"):
            return 1
        else:
            return 
   

class SensorUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView): #113
    template_name = "sensors/edit.html"  
    model = Sensor
    fields = ["idSensor","name","Latitude","Longitude","Temperature","Humidity","Pression","PM25","PM10"]   
    permission_required = "sensors.change_sensor"
    
    def test_func(self):
        if self.request.user.has_perm("sensors.change_sensor"):
            return 1
        else:
            return 


class SensorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  #113
    template_name = "sensors/delete.html"  
    model = Sensor
    success_url = reverse_lazy('sensor_list')
    permission_required = "sensors.delete_sensor"
    
    def test_func(self):
        if self.request.user.has_perm("sensors.delete_sensor"):
            return 1
        else:
            return 
    
class FoliumView(TemplateView):
    template_name = "sensors/sensor_map.html"
    model = Sensor
    
    def get_context_data(self, **kwargs):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # for key, value in kwargs.items():
        #     print("{0} = {1}".format(key, value))
        # print("kwargs")
        print(kwargs["yy"])


        # anyo=2021
        # print(anyo)
        
        datas = datasYY(kwargs["yy"])
        
        m = folium.Map(
            location=[32.6207486, -115.3982056],
            zoom_start=13
            ) 
        
        sensores = Sensor.objects.all()

        for a in sensores:
            popDatos="hola"
            if a.idSensor in datas['Temperature_x']:
                popDatos = (f"""Sensor= {a.name} <br>
                       Temp = {datas['Temperature_x'][a.idSensor]:,.2f} °C<br>
                       Hum = {datas['Humidity_x'][a.idSensor]:,.2f} %<br>
                       Pres = {datas['Pression_x'][a.idSensor]:,.2f} kPa<br>
                       pm 2.5 = {datas['PM25_x'][a.idSensor]:,.4f} µg/m<sup>3</sup><br>
                       pm 10 = {datas['PM10_x'][a.idSensor]:,.4f} µg/m<sup>3</sup><br>
                    """)
            else:
                 popDatos = (f"""Sensor= {a.name} <br>
                       Temp = without data <br>
                       Hum = without data<br>
                       Pres = without data <br>
                       pm 2.5 = without data <br>
                       pm 10 = without data<br>
                    """)             
                
            folium.Marker(
                location=[a.Latitude, a.Longitude],
                tooltip="Click for information",
                popup=folium.Popup(popDatos, max_width=len(f"name= {a.name}")*20),
                icon=folium.Icon(icon='cloud')
            ).add_to(m)

        
        m = m._repr_html_()
        
        Global = generalMeans(kwargs["yy"])
        Temperature = "{:,.2f}".format(Global['Temperature'][0])
        Humidity = "{:,.2f}".format(Global['Humidity'][0])
        Pression = "{:,.2f}".format(Global['Pression'][0])
        PM25 = "{:,.4f}".format(Global['PM25'][0])
        PM10 = "{:,.4f}".format(Global['PM10'][0])
        Dates = "{}".format(Global['vDate'][0])
        Dates2 = "{}".format(Global['vDate2'][0])
        

        
        lista = [2020,2021,2022,2023]
        context ={
            "m": m,
            'Temperature': Temperature,
            'Humidity': Humidity,
            'Pression': Pression,
            'PM25': PM25,
            'PM10' : PM10,
            'fecha': Dates,
            'fecha2': Dates2,
            "lista" : lista,           
        }
        return context
    
    
class SensorTables(TemplateView):
    template_name = "sensors/sensor_table.html"
    model = Sensor
    
    def get_context_data(self, **kwargs):
        # delete_measures()    #delete all mesaurements be careful!!!
        
        print(kwargs["yy"])
        context = tableYY(kwargs["yy"])
        
        Global = generalMeans(kwargs["yy"])
        Temperature = "{:,.2f}".format(Global['Temperature'][0])
        Humidity = "{:,.2f}".format(Global['Humidity'][0])
        Pression = "{:,.2f}".format(Global['Pression'][0])
        PM25 = "{:,.4f}".format(Global['PM25'][0])
        PM10 = "{:,.4f}".format(Global['PM10'][0])
        Dates = "{}".format(Global['vDate'][0])
        Dates2 = "{}".format(Global['vDate2'][0])
        lista = [2020,2021,2022,2023]
        context01 ={
            'Temperature': Temperature,
            'Humidity': Humidity,
            'Pression': Pression,
            'PM25': PM25,
            'PM10' : PM10,
            'fecha': Dates,
            'fecha2': Dates2,
            "lista" : lista,           
        }

        context.update(context01)
        # print(context)
        return context
    
    
 
 
 
 