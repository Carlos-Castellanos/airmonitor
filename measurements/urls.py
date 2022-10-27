from django.urls import path
from .views import(
    # sensor_export_csv, 
    # sensor_import_csv,
    # native_import_csv,
    simple_upload,
    showdata,
    Inicio,
    barras,
    graphs2,
    diary,
)
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views
# from django.conf import settings

urlpatterns = [
    # path('export/', sensor_export_csv, name="measurements_export"),
    # path('import/', sensor_import_csv, name="measurements_import"),
    # path('<native_import/', native_import_csv, name="native_import"),
    path('upload/',simple_upload, name='file_upload'),
    path('showdata/',showdata, name='measurements_showdata'),
    path('showgraphs/',Inicio, name='measurements_graphs'),
    path('barras/',barras, name='measurements_barras'),
    path('graphs2/',graphs2, name='measurements_graphs2'),
    path('', diary, name="measurements_diary"),
    
]
