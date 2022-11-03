import numpy as np
import pandas as pd
# import numpy as np
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
from .models import Measurements

##################################################################
####  Importación de la tabla a un dataframe de panda

#name,measurementDate,measurementTime,Latitude,Longitude,Temperature,Humidity,Pression,PM25,PM10
# item = Measurements.objects.all()

# item.delete()

item = Measurements.objects.all().values()

df = pd.DataFrame(item)
df=df.rename(columns={'idSensor':'Sensor','measurementDate':'MDate','measurementTime':'Time','Latitude':'Lat','Longitude':'Lon','Temperature':'Temp','Humidity':'Hum','Pression':'Pres','PM25':'PM25','PM10':'PM10'})

# convert object to float
df['Lat'] = df['Lat'].astype(float, errors = 'raise')
df['Lon'] = df['Lon'].astype(float, errors = 'raise')
df['Temp'] = df['Temp'].astype(float, errors = 'raise')
df['Hum'] = df['Hum'].astype(float, errors = 'raise')
df['Pres'] = df['Pres'].astype(float, errors = 'raise')
df['PM25'] = df['PM25'].astype(float, errors = 'raise')
df['PM10'] = df['PM10'].astype(float, errors = 'raise')



# convert object to to_datetime
df['MDate'] = pd.to_datetime(df['MDate'])

##################################################################
####  Filtrado y conversion de fechas

## rango de fechas
date1 = "2021-01-01"
date2 = "2021-12-31"
## filtrado por rango
Global = df.loc[(df['MDate'] >= date1) & (df['MDate'] <= date2)]
Monthly = df.loc[(df['MDate'] >= date1) & (df['MDate'] <= date2)]
Yearly = df
## Generacion de etiquetas
List_Dates = Global['MDate'].to_list()
List_Dates = list(set(List_Dates)) 
List_Dates.sort()
Label_Seconds = [x.timestamp()*1000 for x in List_Dates]
col = ['Fech',]
df_Label = pd.DataFrame(Label_Seconds,columns=col)

## group by date
Global = Global.groupby(['MDate']).mean()

## group by month and year
Monthly['Month'] = pd.DatetimeIndex(Monthly['MDate']).month
Monthly['Year'] = pd.DatetimeIndex(Monthly['MDate']).year
# calculate label month
List_Month = Monthly['Month'].to_list()
List_Year =  Monthly['Year'].to_list()
List_MonthYear = []
for i, w in enumerate(List_Year):
    List_MonthYear.append(str(List_Year[i]) + "-" + str(List_Month[i]).zfill(2)+"-01")
List_MonthYear = list(set(List_MonthYear)) 
List_MonthYear.sort()
List_MY_datetime = []
for i, w in enumerate(List_MonthYear):
    List_MY_datetime.append(datetime.strptime(List_MonthYear[i],"%Y-%m-%d"))

Label_SecondsMonth = [x.timestamp()*1000 for x in List_MY_datetime]
df_LabelMonthly = pd.DataFrame(Label_SecondsMonth,columns=col)

Monthly = Monthly.groupby(['Month', 'Year']).mean()


## group by year

Yearly['Year'] = pd.DatetimeIndex(Yearly['MDate']).year
# calculate label month
List_Yy =  Yearly['Year'].to_list()
List_Year = []
for i, w in enumerate(List_Yy):
    List_Year.append(str(List_Yy[i]) + '-01-01')
List_Year.append('2023-01-01')


List_Year = list(set(List_Year)) 
List_Year.sort()
List_Y_datetime = []
for i, w in enumerate(List_Year):
    List_Y_datetime.append(datetime.strptime(List_Year[i],"%Y-%m-%d"))

Label_SecondsYear = [x.timestamp()*1000 for x in List_Y_datetime]
df_LabelYearly = pd.DataFrame(Label_SecondsYear,columns=col)

Yearly = Yearly.groupby(['Year']).mean()



##################################################################
####  Promedio del rango de fechas

Temperature = Global['Temp'].mean() 
Humidity = Global['Hum'].mean()
Pression = Global['Pres'].mean()
PM25 = Global['PM25'].mean()
PM10 = Global['PM10'].mean()


total_res_wor = pd.DataFrame({'Temperature': [Temperature],'Humidity': [Humidity], 'Pression':[Pression] ,'PM25':[PM25],'PM10':[PM10],'vDate':[date1],'vDate2':[date2]})
total_res_wor.fillna(0, inplace=True)


##################################################################
####  Promedio del dia (index.html)

now = datetime.now()
hoy = now.strftime('%Y-%m-%d')

### ajuste por los datos, toma 2021 como si fuera 2022
lastyear = now + relativedelta(years=-1)
format = lastyear.strftime('%Y-%m-%d')
###

daily = df[df['MDate'] == format]   ### corregir por "hoy"
Temperature = daily['Temp'].mean() 
Humidity = daily['Hum'].mean()
Pression = daily['Pres'].mean()
PM25 = daily['PM25'].mean()
PM10 = daily['PM10'].mean()


dailyAVG = pd.DataFrame({'Temperature': [Temperature],'Humidity': [Humidity], 'Pression':[Pression] ,'PM25':[PM25],'PM10':[PM10],'vDate':[hoy]})
dailyAVG.fillna(0, inplace=True)
