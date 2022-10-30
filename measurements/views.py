#import csv
import csv
from distutils.command.upload import upload
from pipes import Template

from django.http import HttpRequest, HttpResponse
from import_export import resources
import numpy as np
from .models import Measurements
from sensors.models import Sensor


from .data import *
import pandas as pd
import json


from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import  render, redirect, get_object_or_404

from .models import Measurements

  
############################################################################################################################################
# Migrate sensos data (upload.html)
    
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
            idsensor = Sensor.objects.get(idSensor=int(row[0]))
            measurements.append(
                Measurements(
                    idSensor = idsensor,
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

        
############################################################################################################################################
# Tresting table (table.html)
def showdata(request):
    item = Measurements.objects.all().values()
    myFrame = pd.DataFrame(item)
    myFrame=myFrame.rename(columns={'idSensor':'Sensor','measurementDate':'Date','measurementTime':'Time','Latitude':'Lat','Longitude':'Lon','Temperature':'Temp','Humidity':'Hum','Pression':'Pres','PM25':'pm2.5','PM10':'pm10'})

    # convert objetc to float
    myFrame['Date'] = pd.to_datetime(myFrame['Date'])
    myFrame['Lat'] = myFrame['Lat'].astype(float, errors = 'raise')
    myFrame['Lon'] = myFrame['Lon'].astype(float, errors = 'raise')
    myFrame['Temp'] = myFrame['Temp'].astype(float, errors = 'raise')
    myFrame['Hum'] = myFrame['Hum'].astype(float, errors = 'raise')
    myFrame['Pres'] = myFrame['Pres'].astype(float, errors = 'raise')
    myFrame['pm2.5'] = myFrame['pm2.5'].astype(float, errors = 'raise')
    myFrame['pm10'] = myFrame['pm10'].astype(float, errors = 'raise')

    #filtrado por fechas
    date1 = "2021-01-01"
    date2 = "2021-01-31"
    df = myFrame.loc[(myFrame['Date'] >= date1) & (myFrame['Date'] <= date2)]
    df = df.groupby(['Date']).mean()
    mydict = {
        "df": df.to_html(classes='table table-striped')
    }

    return render(request, 'measurements/table.html', context=mydict)       
        
############################################################################################################################################
# Global graphs (graphs.html)
def Inicio (request):
    # resumen
    
    Temperature = "{:,.0f}".format(total_res_wor['Temperature'][0])
    Humidity    = "{:,.0f}".format(total_res_wor['Humidity'][0])
    Pression    = "{:,.0f}".format(total_res_wor['Pression'][0])
    PM25   = "{:,.0f}".format(total_res_wor['PM25'][0])
    PM10   = "{:,.0f}".format(total_res_wor['PM10'][0])
    Dates  = "{}".format(total_res_wor['vDate'][0])
    Dates2 = "{}".format(total_res_wor['vDate2'][0])
    
    total_dates       = df_Label['Fech'].tolist()
    total_temperatura = Global['Temp'].tolist()
    total_humedad     = Global['Hum'].tolist()
    total_presion     = Global['Pres'].tolist()
    total_pm25        = Global['PM25'].tolist()
    total_pm10        = Global['PM10'].tolist()
    
    monthly_dates       = df_LabelMonthly['Fech'].tolist()
    monthly_temperatura = Monthly['Temp'].tolist()
    monthly_humedad     = Monthly['Hum'].tolist()
    monthly_presion     = Monthly['Pres'].tolist()
    monthly_pm25        = Monthly['PM25'].tolist()
    monthly_pm10        = Monthly['PM10'].tolist()
    
    yearly_dates       = df_LabelYearly['Fech'].tolist()
    yearly_temperatura = Yearly['Temp'].tolist()
    yearly_humedad     = Yearly['Hum'].tolist()
    yearly_presion     = Yearly['Pres'].tolist()
    yearly_pm25        = Yearly['PM25'].tolist()
    yearly_pm10        = Yearly['PM10'].tolist()
  
    context = {
        # resumen
        'Temperature': Temperature,
        'Humidity': Humidity,
        'Pression': Pression,
        'PM25': PM25,
        'PM10' : PM10,
        'fecha': Dates,
        'fecha2': Dates2,
  
        # Graph dairy
        'total_dates'  : total_dates,
        'total_temperatura' : total_temperatura,
        'total_humedad' : total_humedad,
        'total_presion' : total_presion,
        'total_pm25' : total_pm25, 
        'total_pm10' : total_pm10,               

        # Graph month 
        'monthly_dates'  : monthly_dates,
        'monthly_temperatura' : monthly_temperatura,
        'monthly_humedad' : monthly_humedad,
        'monthly_presion' : monthly_presion,
        'monthly_pm25' : monthly_pm25, 
        'monthly_pm10' : monthly_pm10,     
        
        # Graph year 
        'yearly_dates'  : yearly_dates,
        'yearly_temperatura' : yearly_temperatura,
        'yearly_humedad' : yearly_humedad,
        'yearly_presion' : yearly_presion,
        'yearly_pm25' : yearly_pm25, 
        'yearly_pm10' : yearly_pm10,  
        # Table
        
        "Global": Global.to_html(classes='table table-striped'),
    }

    return render(request,'measurements/graphs.html',context)

############################################################################################################################################
# Sensor Graphs  (graphs2.html)
def graphs2 (request):
    context = { }
    return render(request,'measurements/graphsPlus.html',context)

############################################################################################################################################
# Todays measurements  (home: diary.html)
def diary (request):
    
    Temperature = "{:,.0f}".format(dailyAVG['Temperature'][0])
    Humidity = "{:,.0f}".format(dailyAVG['Humidity'][0])
    Pression = "{:,.0f}".format(dailyAVG['Pression'][0])
    PM25 = "{:,.0f}".format(dailyAVG['PM25'][0])
    PM10 = "{:,.0f}".format(dailyAVG['PM10'][0])
    Dates = "{}".format(dailyAVG['vDate'][0])
   
    
    context = {
        # resumen
        'Temperature': Temperature,
        'Humidity': Humidity,
        'Pression': Pression,
        'PM25': PM25,
        'PM10' : PM10,
        'fecha': Dates,
    }

    return render(request,'measurements/diary.html',context)











