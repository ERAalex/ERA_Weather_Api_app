from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import city_weather
from .serializers import CitySerializers
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .get_weather import get_city_weather




class CityApiView(generics.ListAPIView):
    queryset = city_weather.objects.all()
    serializer_class = CitySerializers

# RetrieveAPIView позволяет выводить конкретную статью по id
class some_cityApiView(RetrieveAPIView):
    queryset = city_weather.objects.all()
    serializer_class = CitySerializers
    # lookup_field - это параметр (поле модели) который в urls набирает пользователь для поиска данных
    # по умолчанию это <int:pk> , теперь поменяем на <str:city_name>
    lookup_field = 'city_name'

    # переосмыслим get тк нам надо достать имя города от пользователя и найти погоду
    def get(self, request, *args, **kwargs):
        # в kwargs храниться наш запрос из urls/<str:city_name> теперь мы можем получить имя запроса и запустить
        # поиск погоды по запросу, потом закинуть в базу и уже выдать пользователю
        name_of_city = kwargs['city_name'].upper()

        # получаем по API погоду из openweather и возвращаем как словарь в переменной diccionary
        diccionary = get_city_weather(name_of_city)

        # если нет данных(например ввели не правильно город) сразу выходим и вернется 'not found'
        if diccionary == None:
            return self.retrieve(request, *args, **kwargs)

        # берем из словаря данные и кидаем в Базу данных, откуда потом Api будет все брать
        check_instance = city_weather.objects.filter(city_name=name_of_city)
        if len(check_instance) == 0:
            new_instance = city_weather.objects.create(
                city_name=name_of_city,
                weather_data=diccionary['temperature'],
            )
        else:
            new_instance = city_weather.objects.filter(city_name=name_of_city).update(
                city_name=name_of_city,
                weather_data=diccionary['temperature'],
            )

        return self.retrieve(request, *args, **kwargs)


