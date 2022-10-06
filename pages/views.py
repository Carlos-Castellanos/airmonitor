from django.shortcuts import render

# from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

class MapsPageView(TemplateView):
    template_name = "maps.html"

class GraphPageView(TemplateView):
    template_name = "graphs.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class GMapsPageView(TemplateView):
    template_name = "gmaps.html"