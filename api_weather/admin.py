from django.contrib import admin
from .models import city_weather

@admin.register(city_weather)
class city_weatherAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'weather_data', 'time']