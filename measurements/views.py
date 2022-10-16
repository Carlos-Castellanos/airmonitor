#import csv
import csv
from distutils.command.upload import upload
from urllib import request
from django.http import HttpRequest, HttpResponse
from import_export import resources
from .models import Measurements

#import daas
from .data import *
import pandas as pd
import json


#import file
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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

from django.shortcuts import  redirect, get_object_or_404

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
        
        
#def native_import_csv(request):
def native_import_csv(myfile):
    # Native Import CSV
    file= "."+myfile
    measurements = []
    with open(file, "r") as csv_file:
        data = list(csv.reader(csv_file, delimiter=","))
        for row in data[1:]:
            measurements.append(
                Measurements(
                    name =row[0],
                    measurementDate =format_date(row[1]),
                    measurementTime =row[2],
                    Latitude =row[3],
                    Longitude =row[4],
                    Temperature=row[5],
                    Humidity =row[6],
                    Pression =row[7],  
                    PM25  =row[8],
                    PM10=row[9],
                )
            )
    if len(measurements) > 0:
        Measurements.objects.bulk_create(measurements)
    print("Successfully imported "+myfile)
    return HttpResponse("Successfully imported")
    
def format_date(mydate):
        import sys
        from datetime import datetime
        print("The original string is : " + str(mydate))
        format = "%Y-%m-%d"
        res = True
        try:
            res = bool(datetime.strptime(mydate, format))
        except ValueError:
            res = False
            objDate = datetime.strptime(mydate, "%d/%m/%Y")
            datetime.strftime(objDate,"%Y-%m-%d")
            print("The new string is : " + str(objDate)[:10])
            return str(objDate)[:10]
        print("Does date match format? : " + str(res))
        return(mydate)
    
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
          
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        print(uploaded_file_url)
        native_import_csv(uploaded_file_url)
        return render(request, 'measurements/upload.html',{
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'measurements/upload.html')
        
#panda
def showdata(request):
    # ['name','measurementDate','measurementTime','Latitude','Longitude','Temperature','Humidity','Pression','PM25','PM10']
    item = Measurements.objects.all().values()
    myFrame = pd.DataFrame(item)
    myFrame=myFrame.rename(columns={'name':'Sensor','measurementDate':'Date','measurementTime':'Time','Latitude':'Lat','Longitude':'Lon','Temperature':'Temp','Humidity':'Hum','Pression':'Pres','PM25':'pm2.5','PM10':'pm10'})

    # convert objetc to float
    myFrame['Date'] = pd.to_datetime(myFrame['Date'])
    myFrame['Lat'] = myFrame['Lat'].astype(float, errors = 'raise')
    myFrame['Lon'] = myFrame['Lon'].astype(float, errors = 'raise')
    myFrame['Temp'] = myFrame['Temp'].astype(float, errors = 'raise')
    myFrame['Hum'] = myFrame['Hum'].astype(float, errors = 'raise')
    myFrame['Pres'] = myFrame['Pres'].astype(float, errors = 'raise')
    myFrame['pm2.5'] = myFrame['pm2.5'].astype(float, errors = 'raise')
    myFrame['pm10'] = myFrame['pm10'].astype(float, errors = 'raise')

    # df = myFrame.head(5)
    df = myFrame[(myFrame['Sensor'] == '2') & (myFrame['Pres'] > 12.39)]
    date2 = "2022-01-01"
    df = myFrame[myFrame['Date'] == date2]
    # df = myFrame.groupby(by = 'Sensor').mean()  error
    # df = myFrame.describe()
    # df = myFrame.groupby(by=['Date']).sum().groupby(level=[0]).cumsum()
    # df = df.groupby(by=['Date']).sum().groupby(level=[0]).cumsum()
    # print(myFrame.info())
    df = myFrame.groupby(['Date']).mean()
    mydict = {
        "df": df.to_html(classes='table table-striped')
    }

    return render(request, 'measurements/table.html', context=mydict)       
        
# graphs

# def getData():
#     return Measurements.objects.filter(
#         estado = True,
#     ).latest('measurementDate')

# def getSensor():
#     return Sensor.objects.filter(
#         estado = True,
#     ).latest('created_on')

def Inicio (request):
    # resumen
    
    Temperature = "{:,.0f}".format(total_res_wor['Temperature'][0])
    Humidity = "{:,.0f}".format(total_res_wor['Humidity'][0])
    Pression = "{:,.0f}".format(total_res_wor['Pression'][0])
    PM25 = "{:,.0f}".format(total_res_wor['PM25'][0])
    PM10 = "{:,.0f}".format(total_res_wor['PM10'][0])
    Dates = "{}".format(total_res_wor['vDate'][0])

    #DailyAverage
    Grafica = {
        "DailyAverage": DailyAverage.to_html(classes='table table-striped')
    }
    # # Contagiados, fallecidos y vacunados

    # fecha_contagios = date_cases_deaths['Fecha'].tolist()
    # total_contagiados = date_cases_deaths['Total contagiados'].tolist()
    # total_fallecidos = date_cases_deaths['Total fallecidos'].tolist()
    # total_vacunados = date_cases_deaths['Total vacunados'].tolist()


    # # 20 primeros paises

    # ## contagios
    # pais20contagios = Country_total_cases_deaths.sort_values('Total contagiados',ascending=False).head(20)
    # N_pais20contagios = pais20contagios['Pais'].tolist()
    # C_pais20contagios = pais20contagios['Total contagiados'].tolist()


    # ## fallecidos
    # pais20fallecidos = Country_total_cases_deaths.sort_values('Total fallecidos',ascending=False).head(20)
    # N_pais20fallecidos = pais20fallecidos['Pais'].tolist()
    # C_pais20fallecidos = pais20fallecidos['Total fallecidos'].tolist()

    # ## vacunados
    # pais20vacunados = Country_total_cases_deaths.sort_values('Total vacunados',ascending=False).head(20)
    # N_pais20vacunados = pais20vacunados['Pais'].tolist()
    # C_pais20vacunados = pais20vacunados['Total vacunados'].tolist()


    # # Continente

    # continentes = Continent_total_cases_deaths.groupby(['Continente']).sum().reset_index()
    # contientesNombre = continentes['Continente'].tolist()
    # continentesContagios = continentes['Total contagiados'].tolist()
    # continentesFallecidos = continentes['Total fallecidos'].tolist()
    # continentesVacunados = continentes['Total vacunados'].tolist()


    # # Table

    
    # json_records = table1.reset_index().to_json(orient ='records')
    # data = []
    # data = json.loads(json_records)

    # # map

    # map_final_contagiados = map_cases_deaths.to_numpy().tolist()
    # map_final_fallecidos = map_final_deaths.to_numpy().tolist()
    # map_final_vacunados = map_final_vaccins.to_numpy().tolist()
    
    context = {

        # resumen
        'Temperature': Temperature,
        'Humidity': Humidity,
        'Pression': Pression,
        'PM25': PM25,
        'PM10' : PM10,
        'fecha': Dates,

        "DailyAverage": DailyAverage.to_html(classes='table table-striped')
    
        # # No por fecha
        # 'fecha_contagios':fecha_contagios,
        # 'total_contagiados':total_contagiados,
        # 'total_fallecidos':total_fallecidos,
        # 'total_vacunados':total_vacunados,


        # # 20 primeros

        # ## 20 contagios
        # 'N_pais20contagios': N_pais20contagios,
        # 'C_pais20contagios': C_pais20contagios,

        # ## 20 fallecidos
        # 'N_pais20fallecidos': N_pais20fallecidos,
        # 'C_pais20fallecidos': C_pais20fallecidos,

        # ## 20 vacunados
        # 'N_pais20vacunados': N_pais20vacunados,
        # 'C_pais20vacunados': C_pais20vacunados,


        # # Contiente
        # 'contientesNombre':contientesNombre,
        # 'continentesContagios': continentesContagios,
        # 'continentesFallecidos': continentesFallecidos,
        # 'continentesVacunados':continentesVacunados,


        # # tabla
        # 'd': data, 

        # # map
        # 'map_final_contagiados':map_final_contagiados,
        # 'map_final_fallecidos':map_final_fallecidos,
        # 'map_final_vacunados':map_final_vacunados,

        # # Redes
        # 'sociales':getData(),
        # 'Sensor':getSensor(),

    }

    return render(request,'measurements/graphs.html',context)