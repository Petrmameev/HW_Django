from django.contrib import admin

from .models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
# Register your models here.

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'created_at']
