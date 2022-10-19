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


# ##################################
# #### Globla data
vDate = "2022-10-18"
Global = df[df["MDate"] == vDate]

# ##################################
# #### Average date from Global dataframe
Temperature = Global['Temp'].mean() 
Humidity = Global['Hum'].mean()
Pression = Global['Pres'].mean()
PM25 = Global['PM25'].mean()
PM10 = Global['PM10'].mean()

total_res_wor = pd.DataFrame({'Temperature': [Temperature],'Humidity': [Humidity], 'Pression':[Pression] ,'PM25':[PM25],'PM10':[PM10],'vDate':[vDate]})
total_res_wor.fillna(0, inplace=True)

# ##################################
# Graphs dairy averange
Global = Global.head(40)

# ##################################
# Table

DailyAverage = Global
