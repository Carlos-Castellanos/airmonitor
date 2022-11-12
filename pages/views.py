from django.shortcuts import render

# from django.shortcuts import render
from django.views.generic import TemplateView



class HomePageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        from measurements.models import Measurements
        from datetime import date
        import pandas as pd
        today = date.today()

        vacio = {'Temperature': "n/a", 'Humidity': "n/a", 'Pression': "n/a", 'PM25': "n/a", 'PM10': "n/a", 'fecha': today.strftime('%y-%m-%d')}
        
        item = Measurements.objects.filter(measurementDate__year=today.year,measurementDate__month=today.month,measurementDate__day=today.day).values()
        
        if (len(item)==0):
            return vacio
        
        df = pd.DataFrame(item)
            # convert object to float
        df['Temperature'] = df['Temperature'].astype(float, errors = 'raise')
        df['Humidity'] = df['Humidity'].astype(float, errors = 'raise')
        df['Pression'] = df['Pression'].astype(float, errors = 'raise')
        df['PM25'] = df['PM25'].astype(float, errors = 'raise')
        
        Temperature = df['Temperature'].mean() 
        Humidity = df['Humidity'].mean()
        Pression = df['Pression'].mean()
        PM25 = df['PM25'].mean()
        PM10 = df['PM10'].mean()
        
        Temperature = "{:,.0f}".format(Temperature)
        Humidity = "{:,.0f}".format(Humidity)
        Pression = "{:,.0f}".format(Pression) 
        PM25 = "{:,.0f}".format(PM25)
        PM10 = "{:,.0f}".format(PM10)
        Dates = "{}".format(today)
        context = {
            # resumen
            'Temperature': Temperature,
            'Humidity': Humidity,
            'Pression': Pression,
            'PM25': PM25,
            'PM10' : PM10,
            'fecha': Dates,
        }

        return context


class MapsPageView(TemplateView):
    template_name = "maps.html"

class GraphPageView(TemplateView):
    template_name = "graphs.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class NoAccesssPageView(TemplateView):
    template_name = "403.html"