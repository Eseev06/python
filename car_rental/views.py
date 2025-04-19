from django.shortcuts import render
from .models import Car  # Импортируем модель Car

def index(request):
    # Получаем 6 последних добавленных автомобилей
    latest_cars = Car.objects.order_by('-id')[:6]
    
    context = {
        'latest_cars': latest_cars,
        'page_title': 'Аренда автомобилей'
    }
    return render(request, 'car_rental/index.html', context)