from django.urls import path
from .views import (
    HomePageView, 
    AboutPageView,
    NoAccesssPageView,

)


urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(), name="about"),
    path('forbidden/',NoAccesssPageView.as_view(), name="forbidden"),
]
