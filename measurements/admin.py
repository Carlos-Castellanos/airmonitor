from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from.models import Measurements    ##add (Register the data base)
admin.site.register(Measurements)  ##add
