import csv
from django.http import HttpResponse
from import_export import resources
from .models import DataSensor

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

    def form_valid(self, form):       #take tha user and save it like datasensor'field
        form.instance.datasensor = self.request.user
        return super().form_valid(form)

# class DataSensorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #113
#     template_name = "DataSensors/edit.html"  
#     model = DataSensor
#     fields = ["title","subtitle","body","image"]  

#     def test_func(self):                                #113
#         obj = self.get_object()
#         return obj.datasensor == self.request.user


# class DataSensorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  #113
#     template_name = "DataSensors/delete.html"  
#     model = DataSensor
#     success_url = reverse_lazy('DataSensor_list')

#     def test_func(self):                                #113
#         obj = self.get_object()
#         return obj.datasensor == self.request.user


# from utils import my_cool_func 
# def view_coolness(request): 
#     data = my_cool_func(request) 
#     return render_to_response("xxx.html")

# csv import - export
#name,measurementDate,measurementTime,Latitude,Longitude,Temperature,Humidity,Pression,PM25,PM10
def export_csv(request):


    # Import-Export library
    datasensor_resource = resources.modelresource_factory(model=DataSensor)()
    dataset = datasensor_resource.export()
    response = HttpResponse(dataset.xls, content_type='text/xls')
    response['Content-Disposition'] = 'atachment; filename="datasensor_library.xls"'
    return response



def import_csv(request):

    # Import-Export library

    with open("data2.csv", "r") as csv_file:
        import tablib

        datasensor_resource = resources.modelresource_factory(model=DataSensor)()
        dataset = tablib.Dataset(headers=[field.name for field in DataSensor._meta.fields]).load(csv_file)
        result = datasensor_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            datasensor_resource.import_data(dataset, dry_run=False)
        return HttpResponse(
            "Successfully imported"
        )