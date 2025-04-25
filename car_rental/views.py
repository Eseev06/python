from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegisterForm  # Импорт своей формы
from .models import Car, Booking




def index(request):
    city = request.GET.get('city')
    search_query = request.GET.get('search')

    cars = Car.objects.all()

    if city:
      cars = cars.filter(city=city)
    if search_query:
      cars = cars.filter(name__icontains=search_query)

# Исключаем автомобили без изображений
    cars = cars.filter(image__isnull=False)

    latest_cars = cars.order_by('-id')[:6]

    login_form = AuthenticationForm()
    register_form = RegisterForm()
    cities = Car.objects.values_list('city', flat=True).distinct()

    context = {
        'latest_cars': latest_cars,
        'page_title': 'Аренда автомобилей',
        'login_form': login_form,
        'register_form': register_form,
        'cities': cities,
        'selected_city': city,
        'search_query': search_query,
    }
    return render(request, 'car_rental/car_list.html', context)  # Обновляем шаблон на car_list.html


@login_required
def my_bookings(request):
    bookings_pending = Booking.objects.filter(user=request.user, status='pending').order_by('-created_at')
    bookings_confirmed = Booking.objects.filter(user=request.user, status='confirmed').order_by('-created_at')
    return render(request, 'car_rental/my_bookings.html', {
        'bookings_pending': bookings_pending,
        'bookings_confirmed': bookings_confirmed,
    })

def faq(request):
    """Представление для страницы FAQ"""
    return render(request, 'car_rental/faq.html', {
        'page_title': 'Вопрос-Ответ',
    })