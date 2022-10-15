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

date_string = df['MDate']

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

# yesterday = date.today()-timedelta(days=1)
# date2 = yesterday.strftime("%Y-%m-%d")
vDate = "2022-01-01"
Global = df[df["MDate"] == vDate]

# other = df[df['Date'] == date2]
# Global = other[other['location'] == 'World']

Temperature = Global['Temp'].sum() 
Humidity = Global['Hum'].sum()
Pression = Global['Pres'].sum()
PM25 = Global['PM25'].sum()
PM10 = Global['PM10'].sum()

total_res_wor = pd.DataFrame({'Temperature': [Temperature],'Humidity': [Humidity], 'Pression':[Pression] ,'PM25':[PM25],'PM10':[PM10],'vDate':[vDate]})
total_res_wor.fillna(0, inplace=True)

# ##################################
# Graphs dairy averange

DailyAverage = df.groupby(['MDate']).mean()

# ##################################
# #### contagio fecha

# Wd = df[df['location'] == 'World']

# ##################################
# #### Mapa Temperature

# other2 = df[df['date'] == date2]
# With_world = other2[other2['location'] != 'World']
# actual = With_world[With_world['location'] != 'International'] 
# actual = actual[actual['location'] != 'Europe']
# actual = actual[actual['location'] != 'North America']
# actual = actual[actual['location'] != 'Asia']
# actual = actual[actual['location'] != 'South America']
# actual = actual[actual['location'] != 'Africa']
# actual = actual[actual['location'] != 'European Union']  
# actual = actual[actual['location'] != 'South Africa']
# actual = actual[actual['location'] != 'Oceania']  
# actual = actual[actual['location'] != 'High income']
# actual = actual[actual['location'] != 'Upper middle income']
# actual = actual[actual['location'] != 'Lower middle income']

# ##################################
# #### For cases and deaths select

# Wd_cases = Wd['total_cases']
# Wd_deaths = Wd['Humidity']
# Wd_people_vaccinated = Wd['people_vaccinated']
# Wd_date = Wd['date']

# date_cases_deaths = pd.concat([Wd_cases, Wd_deaths, Wd_people_vaccinated, Wd_date],   axis=1)


# date_cases_deaths.columns = ['Total contagiados', 'Total fallecidos', 'Total Pression', 'Fecha']

# features = date_cases_deaths.columns

# date_cases_deaths.set_index(['Total contagiados', 'Total fallecidos', 'Total Pression', 'Fecha'])

# date_cases_deaths.fillna(0, inplace=True)


# ##################################
# #### For map select

# iso = actual['iso_code']
# Map_total_cases = actual['total_cases']
# Map_Humidity = actual['Humidity']
# Map_people_vaccinated  = actual['people_vaccinated']
# Pais = actual['location']

# # Contagiados 

# map_cases_deaths = pd.concat([Pais, Map_total_cases], axis=1)

# map_cases_deaths.columns = ['Country', 'Total contagiados']

# map_cases_deaths.fillna(0, inplace=True)

# map_cases_deaths.loc[-1] = ['Country', 'Total contagiados'] 

# map_cases_deaths.index = map_cases_deaths.index + 1

# map_cases_deaths = map_cases_deaths.sort_index()

# # fallecidos

# map_final_deaths = pd.concat([Pais, Map_Humidity], axis=1)

# map_final_deaths.columns = ['Country', 'Total fallecidos']

# map_final_deaths.fillna(0, inplace=True)

# map_final_deaths.loc[-1] = ['Country', 'Total fallecidos'] 

# map_final_deaths.index = map_final_deaths.index + 1

# map_final_deaths = map_final_deaths.sort_index()

# # Vacuandos

# map_final_vaccins = pd.concat([Pais, Map_people_vaccinated], axis=1)

# map_final_vaccins.columns = ['Country', 'Total Pression']

# map_final_vaccins.fillna(0, inplace=True)

# map_final_vaccins.loc[-1] = ['Country', 'Total Pression'] 

# map_final_vaccins.index = map_final_vaccins.index + 1

# map_final_vaccins = map_final_vaccins.sort_index()


# ##################################
# #### For country select

# Country_total_cases = actual['total_cases']
# Country_Humidity = actual['Humidity']
# Country_total_people_vaccinated = actual['people_vaccinated']
# Pais = actual['location']

# Country_total_cases_deaths = pd.concat([Country_total_cases, Country_Humidity, Country_total_people_vaccinated, Pais], axis=1)

# Country_total_cases_deaths.columns = ['Total contagiados', 'Total fallecidos', 'Total Pression', 'Pais']

# ##################################
# #### For continent select

# Continent_total_cases = actual['total_cases']
# Continent_Humidity = actual['Humidity']
# Continent_total_people_vaccinated = actual['people_vaccinated']
# Continente = actual['continent']

# Continent_total_cases_deaths = pd.concat([Continent_total_cases, Continent_Humidity, Continent_total_people_vaccinated, Continente], axis=1)

# Continent_total_cases_deaths.columns = ['Total contagiados', 'Total fallecidos', 'Total Pression', 'Continente']

# Continent_total_cases_deaths.fillna(0, inplace=True)

# ##################################
# #### for table

# # table1 = pd.concat([Pais, Continente, Country_total_cases, Country_Humidity, Country_total_people_vaccinated], axis=1)

# # table1.columns = ['País', 'Continente','Total_contagiados', 'Total_fallecidos', 'Total_Pression']

# table1 = pd.concat([Pais, Country_total_cases, Country_Humidity, Country_total_people_vaccinated], axis=1)

# table1.columns = ['País','Total_contagiados', 'Total_fallecidos', 'Total_Pression']

# table1.fillna(0, inplace=True)


