# filepath: c:\project\anytime123\car_rental\bookings\car_views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return JsonResponse({'cars': list(cars.values())})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return JsonResponse({'car': {'name': car.name, 'brand': car.brand, 'year': car.year, 'price_per_day': car.price_per_day}})