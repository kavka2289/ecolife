from django.urls import path
from . import views

app_name = 'core'  # Пространство имен приложения

urlpatterns = [
    path('', views.index, name='index'),
    path('habits/', views.habit_list, name='habits'),
    path('map/', views.recycling_map, name='recycling_map'),  # Добавьте этот маршрут
]