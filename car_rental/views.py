from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegisterForm  # Импорт своей формы
from .models import Car

def index(request):
    city = request.GET.get('city')  # Получаем город из параметров запроса
    if city:
        latest_cars = Car.objects.filter(city=city).order_by('-id')[:6]  # Фильтруем по городу
    else:
        latest_cars = Car.objects.order_by('-id')[:6]  # Показываем последние 6 машин

    login_form = AuthenticationForm()
    register_form = RegisterForm()
    cities = Car.CITY_CHOICES  # Используем фиксированный список городов из модели

    context = {
        'latest_cars': latest_cars,
        'page_title': 'Аренда автомобилей',
        'login_form': login_form,
        'register_form': register_form,
        'cities': [choice[0] for choice in cities],  # Передаём только названия городов
        'selected_city': city,
    }
    return render(request, 'car_rental/index.html', context)