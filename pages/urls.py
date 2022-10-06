from unicodedata import name
from django.urls import path
from .views import (
    HomePageView, 
    MapsPageView,
    GraphPageView,
    AboutPageView,
    GMapsPageView
)


urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('maps/',MapsPageView.as_view(), name='maps'),
    path('graphs/',GraphPageView.as_view(), name='graphs'),
    path('about/',AboutPageView.as_view(), name="about"),
    path('gmaps/',GMapsPageView.as_view(), name="gmaps"),
]
