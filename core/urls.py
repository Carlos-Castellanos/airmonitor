from django.urls import path

from core.views import export_csv, import_csv

urlpatterns = [
    path('export/', export_csv),
    path('import/', import_csv),
]