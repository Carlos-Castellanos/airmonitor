from django.urls import path
from .views import(
    DataSensorListView,
    # DataSensorDetailView,
    DataSensorCreateView,
    # DataSensorDeleteView,
    # DataSensorUpdateView
)
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views
# from django.conf import settings


urlpatterns = [
    path('',DataSensorListView.as_view() , name="DataSensor_list"),
    # path('<int:pk>/', DataSensorDetailView.as_view(), name="DataSensor_detail"),
    path('new/', DataSensorCreateView.as_view(), name="DataSensor_new"),
    # path('<int:pk>/delete/', DataSensorDeleteView.as_view(), name="DataSensor_delete"),
    # path('<int:pk>/edit/', DataSensorUpdateView.as_view(), name="DataSensor_edit"),

]