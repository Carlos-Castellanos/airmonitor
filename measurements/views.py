import csv
from django.http import HttpResponse
from import_export import resources
from .models import Measurements

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
from .models import Measurements

# Create your views here.

class MeasurementsListView(ListView):
    template_name = "measurements/list.html"   
    model = Measurements


# class measurementsDetailView(DetailView):
#     template_name = "measurements/detail.html"  
#     model = Measurements

class MeasurementsCreateView(LoginRequiredMixin, CreateView): #113
    template_name = "measurements/new.html"  
    model = Measurements
    fields = ["measurementDate","Latitude","Longitude","Temperature","Humidity","Pression","PM25","PM10","sensor"]  

    def form_valid(self, form):       #take tha user and save it like measurements'field
        form.instance.Measurements = self.request.user
        return super().form_valid(form)

# class measurementsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #113
#     template_name = "measurements/edit.html"  
#     model = Measurements
#     fields = ["title","subtitle","body","image"]  

#     def test_func(self):                                #113
#         obj = self.get_object()
#         return obj.measurements == self.request.user


# class measurementsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  #113
#     template_name = "measurements/delete.html"  
#     model = Measurements
#     success_url = reverse_lazy('measurements_list')

#     def test_func(self):                                #113
#         obj = self.get_object()
#         return obj.measurements == self.request.user


# from utils import my_cool_func 
# def view_coolness(request): 
#     measurements = my_cool_func(request) 
#     return render_to_response("xxx.html")

# csv import - export
#name,measurementDate,measurementTime,Latitude,Longitude,Temperature,Humidity,Pression,PM25,PM10
def sensor_export_csv(request):


    # Import-Export library
    measurements_resource = resources.modelresource_factory(model=Measurements)()
    dataset = measurements_resource.export()
    response = HttpResponse(dataset.xls, content_type='text/xls')
    response['Content-Disposition'] = 'atachment; filename="measurements_library.xls"'
    return response



def sensor_import_csv(request):

    # Import-Export library

    with open("measurements4.csv", "r") as csv_file:
        import tablib

        measurements_resource = resources.modelresource_factory(model=Measurements)()
        dataset = tablib.Dataset(headers=[field.name for field in Measurements._meta.fields]).load(csv_file)
        result = measurements_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            measurements_resource.import_data(dataset, dry_run=False)
        return HttpResponse(
            "Successfully imported"
        )