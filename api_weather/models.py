from django.db import models



class city_weather(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    city_name = models.CharField('Название города', max_length=200, null=True)
    weather_data = models.CharField('данные по погоде', max_length=200, null=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city_name


    class Meta:
        verbose_name = 'Город - погода'
        verbose_name_plural = 'Город - погода'

