from django.shortcuts import render, get_object_or_404
from car_rental.models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_rental/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_rental/car_detail.html', {'car': car})
