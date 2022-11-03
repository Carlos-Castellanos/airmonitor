import numpy as np
import pandas as pd
# import numpy as np
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
from measurements.models import Measurements
from sensors.models import Sensor

#################################################################
###  Importación de la tabla a un dataframe de panda

#name,measurementDate,measurementTime,Latitude,Longitude,Temperature,Humidity,Pression,PM25,PM10

def datasYY(myYear):

    ## rango de fechas del año seleccionado
    date1 = str(myYear) + '-01-01'
    date2 = str(myYear) + '-12-31'
    
    item = Measurements.objects.all().values()
    sensors = Sensor.objects.all().values()   
    
    df = pd.DataFrame(item)
    df_sensors = pd.DataFrame(sensors)
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


    
    ## filtrado por rango
    df = df.loc[(df['MDate'] >= date1) & (df['MDate'] <= date2)]

    df = df.drop(['Time','MDate'], axis=1)

    df = pd.merge(df, df_sensors, left_on='idSensor_id', right_on='idSensor')

    # ## group by sensor
    df = df.groupby(['idSensor_id']).mean()

    # ## group by year

    # for i in range(len(df)):
    #     print(df.iloc[i]['idSensor'])
    #     print(df.iloc[i]['Temp'])
    
    dictionarySensor = df.to_dict()
    # print(dictionarySensor)
    
    return (dictionarySensor)
    
def generalMeans(myYear):

    item = Measurements.objects.all().values()
    sensors = Sensor.objects.all().values()   
    
    df = pd.DataFrame(item)
    df_sensors = pd.DataFrame(sensors)
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

    ## rango de fechas del año seleccionado
    date1 = str(myYear) + '-01-01'
    date2 = str(myYear) + '-12-31'
    
    ## filtrado por rango
    df = df.loc[(df['MDate'] >= date1) & (df['MDate'] <= date2)]
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

