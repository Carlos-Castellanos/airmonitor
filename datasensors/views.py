from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import( 
    CreateView, 
    # DeleteView,
    # UpdateView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
   )   #113

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# https://docs.djangoproject.com/en/4.1/ref/class-based-views/flattened-index/
from django.urls import reverse_lazy
from .models import DataSensor

# Create your views here.

class DataSensorListView(ListView):
    template_name = "DataSensors/list.html"   
    model = DataSensor


# class DataSensorDetailView(DetailView):
#     template_name = "DataSensors/detail.html"  
#     model = DataSensor

class DataSensorCreateView(LoginRequiredMixin, CreateView): #113
    template_name = "DataSensors/new.html"  
    model = DataSensor
    fields = ["measurementDateTime","Latitude","Longitude","Temperature","Humidity","Pression","PM25","PM10","sensor"]  

    def form_valid(self, form):       #take tha user and save it like author'field
        form.instance.author = self.request.user
        return super().form_valid(form)

# class DataSensorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #113
#     template_name = "DataSensors/edit.html"  
#     model = DataSensor
#     fields = ["title","subtitle","body","image"]  

#     def test_func(self):                                #113
#         obj = self.get_object()
#         return obj.author == self.request.user


# class DataSensorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  #113
#     template_name = "DataSensors/delete.html"  
#     model = DataSensor
#     success_url = reverse_lazy('DataSensor_list')

#     def test_func(self):                                #113
#         obj = self.get_object()
#         return obj.author == self.request.user


# from utils import my_cool_func 
# def view_coolness(request): 
#     data = my_cool_func(request) 
#     return render_to_response("xxx.html")

