from django.urls import path
from .views import CityApiView, some_cityApiView


urlpatterns = [
    path('api/v1/city/', CityApiView.as_view()),
    # вывод конкретной статьи - города благодаря RetrieveAPIView
    path('api/v1/city/<str:city_name>', some_cityApiView.as_view()),
]
