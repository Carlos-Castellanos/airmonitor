# AirMonitor System

## Project Description
This system allows you to keep track of temperature, humidity, ambient pressure, pm2.5 and pm10 measurements in your city or area of interest, through multiple sensors distributed throughout the city of Mexicali. The system allows any user to visualize the current measurements, however this system is aimed at air quality researchers, users of this type, have the ability to access annual, monthly and daily graphs where they can analyze the behavior of air quality through the five indicators (temperature, humidity, ambient pressure, pm2.5 and pm10). In addition, they can see on maps the geolocation of the sensors and the average measurements that exist in each one of them. 

To analyze the raw data, it is also possible to view the actual measurements in a given period of time, which gives the possibility to work according to the areas of interest. Research users have access to the list of active sensors and their exact geolocation.

Finally, the system has an administrator user, who has the power to manage the sensors, update the information collected by the sensors through csv files (stored in the folder data.csv 2020.csv, 2021.csv and 2022.csv; For testing purposes the data were randomly generated).

## The functionality it has (what works and what doesn't).
The system complies with the loading of csv files, the CRUD of the sensors, the validation of users (administrator, researcher and anonymous), generates the mapping of the sensors and displays the data according to the selected period, displays the data in tabular form also filtered by time periods. on the main screen presents the average of medicines of the current date and for the temperature indicators, pm 25. and pm10 uses a color code in the box where they are displayed according to the level of risk.
The graphs section displays information for the year 2021 (the option to change the year has not been integrated) and allows the data to be filtered for that period, either by a specific period of time or averaged by day, month or year. Additionally, the option to zoom in and out has been integrated.
The functions of the "measurements" app have yet to be migrated to classes.

Some validations, for example if the database is empty the graphs page crashes. This is validated in the sensor map, the main page and the table but not in the graphs. The Change password option is not functional, the email part was not configured

## The technologies used
crispy-bootstrap5==0.7
Django==4.1.2
django-admin-rangefilter==0.9.0
django-crispy-forms==1.14.0
django-import-export==2.9.0
folium==0.13.0
Jinja2==3.1.2
numpy==1.23.3
pandas==1.5.0
Python 3.8.10
Javascripy
Graph.js==3.1

## The steps to run the project
The main menu consists of Home, Graphs, Maps, Maps, Tables, Sensors and Login.

### Home: 
It is the main page and has information about the measurements of the indicators of the current date.

### Graphs: 
Allows you to view the graphs, with the selection of period, which can be daily, i.e. all the average daily measurements during the year; monthly, the average monthly measurements of the year; and finally annual, the average annual measurements of all the years.
Additionally, at the bottom you can select a specific period of dates, the filter button is to expand the selected period and the reset button is to return to the daily measurements of the whole year.
A relevant point is that you can also zoom by selecting with the mouse a specific area of the graph, the reset button will restore the original graph.

### Maps: 
In this section a map is displayed indicating the points where the sensors are located, by clicking on them you can see the average information of each indicator of that sensor. You can select whether the information is annual (indicating the desired year), monthly (indicating year and month) and finally daily (indicating the specific day).

### Tables: 
This option displays in tabular form the complete information, without averaging filter, for a period of time. This can be a whole year, a single month or a particular day.

### Sensor: 
This option has a submenu:
#### upload information: 
Allows to upload the information collected by the sensors, only the administrator user.
#### List Sensor: 
Displays the information of the sensors, only research users and administrators can see them, and only the latter can edit or delete them.
#### New Sensor: Allows the administrator user to create new sensors.

### Login has several options:
#### Login: 
Allows the authorized user to register in the system to log in
#### Logout: 
Allows to end the session
#### Change password: 
Allows you to change the user's password
#### Singup: 
Allows anyone to create an account, however that account does not have any additional access, the administrator will be the one who assigns the privileges of researcher or in his case of administrator
