from django.shortcuts import render
from .models import EcoHabit, RecyclingPoint  # Импортируем нужные модели

def index(request):
    return render(request, 'ecolife/index.html')

def habit_list(request):
    habits = EcoHabit.objects.all()  # Получаем все привычки из БД
    return render(request, 'ecolife/habits.html', {'habits': habits})

def recycling_map(request):
    points = RecyclingPoint.objects.all()  # Получаем все пункты переработки
    return render(request, 'ecolife/map.html', {'points': points})