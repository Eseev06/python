from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegisterForm  # Импорт своей формы
from .models import Car, Booking

def index(request):
    city = request.GET.get('city')  # Получаем город из параметров запроса
    if city:
        latest_cars = Car.objects.filter(city=city).order_by('-id')[:6]  # Фильтруем по городу
    else:
        latest_cars = Car.objects.order_by('-id')[:6]  # Показываем последние 6 машин

    login_form = AuthenticationForm()
    register_form = RegisterForm()
    cities = Car.objects.values_list('city', flat=True).distinct()  # Получаем уникальные города из базы данных

    context = {
        'latest_cars': latest_cars,
        'page_title': 'Аренда автомобилей',
        'login_form': login_form,
        'register_form': register_form,
        'cities': cities,  # Передаём список городов
        'selected_city': city,
    }
    return render(request, 'car_rental/index.html', context)

@login_required
def my_bookings(request):
    bookings_pending = Booking.objects.filter(user=request.user, status='pending').order_by('-created_at')
    bookings_confirmed = Booking.objects.filter(user=request.user, status='confirmed').order_by('-created_at')
    return render(request, 'car_rental/my_bookings.html', {
        'bookings_pending': bookings_pending,
        'bookings_confirmed': bookings_confirmed,
    })