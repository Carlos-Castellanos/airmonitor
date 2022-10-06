from django.urls import path
from .views import(
    SensorListView,
    SensorDetailView,
    SensorCreateView,
    SensorDeleteView,
    SensorUpdateView
)
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views
# from django.conf import settings


urlpatterns = [
    path('',SensorListView.as_view() , name="sensor_list"),
    path('<int:pk>/', SensorDetailView.as_view(), name="sensor_detail"),
    path('new/', SensorCreateView.as_view(), name="sensor_new"),
    path('<int:pk>/delete/', SensorDeleteView.as_view(), name="sensor_delete"),
    path('<int:pk>/edit/', SensorUpdateView.as_view(), name="sensor_edit"),

]