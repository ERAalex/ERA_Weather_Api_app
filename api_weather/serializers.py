from rest_framework import serializers
from .models import city_weather

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = city_weather
        fields = ('city_name', 'weather_data')