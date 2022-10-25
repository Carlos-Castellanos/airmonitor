import numpy as np
import pandas as pd
# import numpy as np
from datetime import date, timedelta, datetime
from .models import Measurements

#name,measurementDate,measurementTime,Latitude,Longitude,Temperature,Humidity,Pression,PM25,PM10
item = Measurements.objects.all().values()
df = pd.DataFrame(item)
df=df.rename(columns={'name':'Sensor','measurementDate':'MDate','measurementTime':'Time','Latitude':'Lat','Longitude':'Lon','Temperature':'Temp','Humidity':'Hum','Pression':'Pres','PM25':'PM25','PM10':'PM10'})

# convert object to float
df['Lat'] = df['Lat'].astype(float, errors = 'raise')
df['Lon'] = df['Lon'].astype(float, errors = 'raise')
df['Temp'] = df['Temp'].astype(float, errors = 'raise')
df['Hum'] = df['Hum'].astype(float, errors = 'raise')
df['Pres'] = df['Pres'].astype(float, errors = 'raise')
df['PM25'] = df['PM25'].astype(float, errors = 'raise')
df['PM10'] = df['PM10'].astype(float, errors = 'raise')

##################################################################
####  Filtrado y conversion de fechas 
print("***********************************************************")
print("************************************************* original")
print(df.info())
# primero de enero de 2021 = 1659398400000000000     1609459200.0
df['MDate'] = pd.to_datetime(df['MDate'])
date1 = "2021-01-01"
date2 = "2021-12-31"
Global = df.loc[(df['MDate'] >= date1) & (df['MDate'] <= date2)]
List_Dates = Global['MDate'].to_list()
List_Dates = list(set(List_Dates)) 
List_Dates.sort()
Label_Seconds = [x.timestamp()*1000 for x in List_Dates]
col = ['Fech',]
df_Label = pd.DataFrame(Label_Seconds,columns=col)

print('**************************  fech')
print(df_Label)
print(df_Label.info())
  
    
# d = datetime.fromtimestamp(1577844540000//1000)
# d.timestamp()*1000
    
Global = Global.groupby(['MDate']).mean()
print("************************************************* filtrada")

#gg = pd.to_timedelta(Global['MDate'], unit='ns').dt.total_seconds().astype(int)
##################################################################

# una_fecha = '2021-01-01'
# fecha_dt = datetime.strptime(una_fecha, '%Y-%m-%d')
# time_epoc = datetime.strptime(una_fecha, '%Y-%m-%d').timestamp()
# time_epoc = datetime.strptime("2021/01/01 00:00:00", "%Y/%m/%d %H:%M:%S").timestamp()
# print(fecha_dt)
# print(time_epoc)



##################################################################
# #### Average date from Global dataframe

vDate = "2022-10-18"
Temperature = Global['Temp'].mean() 
Humidity = Global['Hum'].mean()
Pression = Global['Pres'].mean()
PM25 = Global['PM25'].mean()
PM10 = Global['PM10'].mean()


total_res_wor = pd.DataFrame({'Temperature': [Temperature],'Humidity': [Humidity], 'Pression':[Pression] ,'PM25':[PM25],'PM10':[PM10],'vDate':[vDate]})
total_res_wor.fillna(0, inplace=True)



