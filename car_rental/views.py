from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegisterForm  # Импорт своей формы
from .models import Car

def index(request):
    latest_cars = Car.objects.order_by('-id')[:6]
    
    login_form = AuthenticationForm()
    register_form = RegisterForm()

    context = {
        'latest_cars': latest_cars,
        'page_title': 'Аренда автомобилей',
        'login_form': login_form,
        'register_form': register_form
    }
    return render(request, 'car_rental/index.html', context)
