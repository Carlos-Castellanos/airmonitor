import pandas as pd
# import numpy as np
from datetime import date, timedelta, datetime
from .models import Measurements
#name,measurementDate,measurementTime,Latitude,Longitude,Temperature,Humidity,Pression,PM25,PM10
item = Measurements.objects.all().values()
df = pd.DataFrame(item)
df=df.rename(columns={'name':'Sensor','measurementDate':'MDate','measurementTime':'Time','Latitude':'Lat','Longitude':'Lon','Temperature':'Temp','Humidity':'Hum','Pression':'Pres','PM25':'PM25','PM10':'PM10'})

# convert objetc to float
df['MDate'] = pd.to_datetime(df['MDate'])
df['Lat'] = df['Lat'].astype(float, errors = 'raise')
df['Lon'] = df['Lon'].astype(float, errors = 'raise')
df['Temp'] = df['Temp'].astype(float, errors = 'raise')
df['Hum'] = df['Hum'].astype(float, errors = 'raise')
df['Pres'] = df['Pres'].astype(float, errors = 'raise')
df['PM25'] = df['PM25'].astype(float, errors = 'raise')
df['PM10'] = df['PM10'].astype(float, errors = 'raise')



DF_Sensor = df['Sensor']
DF_Date = df['MDate']
DF_Time = df['Time']
DF_Lat = df['Lat']
DF_Lon = df['Lon']
DF_Temp = df['Temp']
DF_Hum = df['Hum']
DF_Pres = df['Pres']
DF_PM25 = df['PM25']
DF_PM10 = df['PM10']


DF_total = pd.concat([DF_Sensor, DF_Date, DF_Time, DF_Lat, DF_Lon, DF_Temp,DF_Hum,DF_Pres,DF_PM25,DF_PM10], axis=1)

DF_total.columns = ['Sensor','Date','Time','Latitude','Longitude','Temperature','Humidity','Pression','PM 2.5','PM 10']


# ##################################
# #### Tabla resumen

vDate = "2022-01-01"
Global = df[df["MDate"] == vDate]

Temperature = Global['Temp'].mean() 
Humidity = Global['Hum'].mean()
Pression = Global['Pres'].mean()
PM25 = Global['PM25'].mean()
PM10 = Global['PM10'].mean()

total_res_wor = pd.DataFrame({'Temperature': [Temperature],'Humidity': [Humidity], 'Pression':[Pression] ,'PM25':[PM25],'PM10':[PM10],'vDate':[vDate]})
total_res_wor.fillna(0, inplace=True)

# ##################################
# Graphs dairy averange

DailyAverage = df.groupby(['MDate']).mean()

Global = Global.head(6)
GlobalTemp = Global['Temp']
GlobalHum = Global['Hum']
GlobalPress = Global['Pres']
GlobalPM25 = Global['PM25']
GlobalPM10 = Global['PM10']

