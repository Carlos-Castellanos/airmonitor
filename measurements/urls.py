from django.urls import path
from .views import(
    MeasurementsListView,
    # MeasurementsDetailView,
    MeasurementsCreateView,
    # MeasurementsDeleteView,
    # MeasurementsUpdateView,
    sensor_export_csv, 
    sensor_import_csv,
)
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views
# from django.conf import settings


urlpatterns = [
    path('',MeasurementsListView.as_view() , name="measurements_list"),
    # path('<int:pk>/', MeasurementsDetailView.as_view(), name="measurements_detail"),
    path('new/', MeasurementsCreateView.as_view(), name="measurements_new"),
    # path('<int:pk>/delete/', MeasurementsDeleteView.as_view(), name="measurements_delete"),
    # path('<int:pk>/edit/', MeasurementsUpdateView.as_view(), name="measurements_edit"),
    path('export/', sensor_export_csv, name="measurements_export"),
    path('import/', sensor_import_csv, name="measurements_import"),

]