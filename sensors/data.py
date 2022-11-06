from django.shortcuts import render
import numpy as np
import pandas as pd
# import numpy as np
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
from requests import request
from measurements.models import Measurements
from sensors.models import Sensor

#################################################################
###  Importación de la tabla a un dataframe de panda

#name,measurementDate,measurementTime,Latitude,Longitude,Temperature,Humidity,Pression,PM25,PM10

def datasYY(myPeriodo):
    # ## rango de fechas del periodo seleccionado
    
    vacio = {'Latitude_x': {}, 'Longitude_x': {}, 'Temperature_x': {}, 'Humidity_x': {}, 'Pression_x': {}, 'PM25_x': {}, 'PM10_x': {}, 'id': {}, 'idSensor': {}, 'Temperature_y': {}, 'Humidity_y': {}, 'Pression_y': {}, 'PM25_y': {}, 'PM10_y': {}}
    
    fecha=str(myPeriodo).split('-')
    AA=fecha[0]
    MM=f'{int(fecha[1]):02d}'
    DD=f'{int(fecha[2]):02d}'
    try:
        if MM=="00":
            # print("maps Anual")
            item = Measurements.objects.filter(measurementDate__year=AA).values()
        elif DD=="00":
            # print("maps Mensual")
            item = Measurements.objects.filter(measurementDate__year=AA,measurementDate__month=MM).values()
        else:
            # print("maps Dia")
            item = Measurements.objects.filter(measurementDate__year=AA,measurementDate__month=MM,measurementDate__day=DD).values()
    except ValueError:
        return vacio
    
    if (len(item)==0):
        return vacio
    ##Sensors list
    sensors = Sensor.objects.all().values()  
     
    ## Convert queryset to dataframe
    df = pd.DataFrame(item)
    df_sensors = pd.DataFrame(sensors)
    # df=df.rename(columns={'idSensor':'Sensor','measurementDate':'measurementDate','measurementTime':'Time','Latitude':'Lat','Longitude':'Lon','Temperature':'Temp','Humidity':'Hum','Pression':'Pres','PM25':'PM25','PM10':'PM10'})


    # convert object to float
    df['Latitude'] = df['Latitude'].astype(float, errors = 'raise')
    df['Longitude'] = df['Longitude'].astype(float, errors = 'raise')
    df['Temperature'] = df['Temperature'].astype(float, errors = 'raise')
    df['Humidity'] = df['Humidity'].astype(float, errors = 'raise')
    df['Pression'] = df['Pression'].astype(float, errors = 'raise')
    df['PM25'] = df['PM25'].astype(float, errors = 'raise')
    df['PM10'] = df['PM10'].astype(float, errors = 'raise')
    # convert object to to_datetime
    df['measurementDate'] = pd.to_datetime(df['measurementDate'])

    ## filtrado por rango
   ############################# df = df.loc[(df['measurementDate'] >= date1) & (df['measurementDate'] <= date2)]

    df = df.drop(['measurementTime','measurementDate'], axis=1)

    df = pd.merge(df, df_sensors, left_on='idSensor_id', right_on='idSensor')
    # ## group by sensor
    df = df.groupby(['idSensor_id']).mean()
    # ## group by year
    
    dictionarySensor = df.to_dict()
    
    return (dictionarySensor)


def tableYY(myPeriodo):
    # ## rango de fechas del periodo seleccionado
    
    vacio = {'Latitude_x': {}, 'Longitude_x': {}, 'Temperature_x': {}, 'Humidity_x': {}, 'Pression_x': {}, 'PM25_x': {}, 'PM10_x': {}, 'id': {}, 'idSensor': {}, 'Temperature_y': {}, 'Humidity_y': {}, 'Pression_y': {}, 'PM25_y': {}, 'PM10_y': {}}
    
    fecha=str(myPeriodo).split('-')
    AA=fecha[0]
    MM=f'{int(fecha[1]):02d}'
    DD=f'{int(fecha[2]):02d}'
    try:
        if MM=="00":
            # print("maps Anual")
            item = Measurements.objects.filter(measurementDate__year=AA).values()
        elif DD=="00":
            # print("maps Mensual")
            item = Measurements.objects.filter(measurementDate__year=AA,measurementDate__month=MM).values()
        else:
            # print("maps Dia")
            item = Measurements.objects.filter(measurementDate__year=AA,measurementDate__month=MM,measurementDate__day=DD).values()
    except ValueError:
        return vacio
    
    if (len(item)==0):
        return vacio
     
    ## Convert queryset to dataframe
    df = pd.DataFrame(item)

    # convert object to float
    df['Latitude'] = df['Latitude'].astype(float, errors = 'raise')
    df['Longitude'] = df['Longitude'].astype(float, errors = 'raise')
    df['Temperature'] = df['Temperature'].astype(float, errors = 'raise')
    df['Humidity'] = df['Humidity'].astype(float, errors = 'raise')
    df['Pression'] = df['Pression'].astype(float, errors = 'raise')
    df['PM25'] = df['PM25'].astype(float, errors = 'raise')
    df['PM10'] = df['PM10'].astype(float, errors = 'raise')
    # convert object to to_datetime
    df['measurementDate'] = pd.to_datetime(df['measurementDate'])

    # 'Sensor':[df['idSensor']],
    df01 = pd.DataFrame({'Temperature': [df['Temperature']],'Humidity': [df['Humidity']], 'Preasure':[df['Pression']] ,'PM25':[df['PM25']],'PM10':[df['PM10']],'Date':[df['measurementDate']]})
    
    df01.fillna(0, inplace=True)
    
    mydict = {
        "df": df.to_html(classes='table table-striped')
    }

    return mydict
    
    
    
    
def generalMeans(myPeriodo):
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    vacio = pd.DataFrame({'Temperature': [0],'Humidity': [0], 'Pression':[0] ,'PM25':[0],'PM10':[0],'vDate':["No info"],'vDate2':[""]})

    # ## rango de fechas del periodo seleccionado
    fecha=str(myPeriodo).split('-')
    AA=fecha[0]
    m=int(fecha[1])
    d=int(fecha[2])
    MM=f'{int(fecha[1]):02d}'
    DD=f'{int(fecha[2]):02d}'
    try:   
        if m==0:
            # print("m==0 Anual")
            item = Measurements.objects.filter(measurementDate__year=AA).values()
            date1 = "Year "+AA
            date2 = ""
        elif d==0 :
            # print("d=0 Mensual")
            item = Measurements.objects.filter(measurementDate__year=AA,measurementDate__month=MM).values()
            date1 = months[m-1]+" "+AA
            date2 = '' 
        else:
            # print("else  Dia")
            item = Measurements.objects.filter(measurementDate__year=AA,measurementDate__month=MM,measurementDate__day=DD).values()
            date1 = months[m-1] + ' ' + f'{int(fecha[2]):02d}'+ " "+AA 
            date2 = ""
        
    except ValueError:
        return vacio

    if (len(item)==0):
        return vacio
    
    df = pd.DataFrame(item)
    df=df.rename(columns={'idSensor':'Sensor','measurementDate':'measurementDate','measurementTime':'Time','Latitude':'Lat','Longitude':'Lon','Temperature':'Temp','Humidity':'Hum','Pression':'Pres','PM25':'PM25','PM10':'PM10'})

    # convert object to float
    df['Lat'] = df['Lat'].astype(float, errors = 'raise')
    df['Lon'] = df['Lon'].astype(float, errors = 'raise')
    df['Temp'] = df['Temp'].astype(float, errors = 'raise')
    df['Hum'] = df['Hum'].astype(float, errors = 'raise')
    df['Pres'] = df['Pres'].astype(float, errors = 'raise')
    df['PM25'] = df['PM25'].astype(float, errors = 'raise')
    df['PM10'] = df['PM10'].astype(float, errors = 'raise')
    # convert object to to_datetime
    df['measurementDate'] = pd.to_datetime(df['measurementDate'])

    # ##################################################################
    # ####  Promedio general para imprimir en html

    Temperature = df['Temp'].mean() 
    Humidity = df['Hum'].mean()
    Pression = df['Pres'].mean()
    PM25 = df['PM25'].mean()
    PM10 = df['PM10'].mean()

    Global = pd.DataFrame({'Temperature': [Temperature],'Humidity': [Humidity], 'Pression':[Pression] ,'PM25':[PM25],'PM10':[PM10],'vDate':[date1],'vDate2':[date2]})
    Global.fillna(0, inplace=True)
    
    return (Global)

