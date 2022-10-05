from unicodedata import name
from django.urls import path
from .views import (
    HomePageView, 
    MapsPageView,
    GraphPageView,
    SensorPageView,
    AdminSensorPageView,
    AboutPageView,
    GMapsPageView
)


urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('maps/',MapsPageView.as_view(), name='maps'),
    path('graphs/',GraphPageView.as_view(), name='graphs'),
    path('sensor/',SensorPageView.as_view(), name='sensor'),
    path('adminsensor/',AdminSensorPageView.as_view(), name='adminsensor'),
    path('about/',AboutPageView.as_view(), name="about"),
    path('gmaps/',GMapsPageView.as_view(), name="gmaps"),
]
