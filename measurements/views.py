#import csv
import csv
from distutils.command.upload import upload
#from urllib import request
from django.http import HttpRequest, HttpResponse
from import_export import resources
from .models import Measurements
#import daas
from .data import *
import pandas as pd
import json
#import file
#from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import  render, redirect, get_object_or_404
#from django.urls import reverse_lazy
from .models import Measurements

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
        
# Tresting table (table.html)
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
    # # Temperatura, humedad, presion pm25 y pm10


    total_temperatura = Global['Temp'].tolist()
    total_humedad = Global['Hum'].tolist()
    total_presion = Global['Pres'].tolist()
    total_pm25 = Global['PM25'].tolist()
    total_pm10 = Global['PM10'].tolist()
    
    #fecha_mediciones = Global['MDate'].tolist()  
    fecha_mediciones = ["aa", "bb", "cc", "dd", "ee", "ff"]


    context = {
        # resumen
        'Temperature': Temperature,
        'Humidity': Humidity,
        'Pression': Pression,
        'PM25': PM25,
        'PM10' : PM10,
        'fecha': Dates,
  
        # Graph

        'total_temperatura' : total_temperatura,
        'total_humedad' : total_humedad,
        'total_presion' : total_presion,
        'total_pm25' : total_pm25, 
        'total_pm10' : total_pm10,               
        'fecha_mediciones' : fecha_mediciones,
        
        
        
        # Table
        "DailyAverage": DailyAverage.to_html(classes='table table-striped'),
    }

    return render(request,'measurements/graphs.html',context)

    
def barras(request):
    products = Measurements.objects.all()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ProductForm()        
    context = {
        "products": products,
        # "form": form
    }
    return render(request, 'measurements/barras.html', context)










