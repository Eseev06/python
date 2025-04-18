from django.shortcuts import render

# Create your views here.from django.shortcuts import render, get_object_or_404
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_detail(request, pk):
    car =  (Car, pk=pk)
    return render(request, 'car_detail.html', {'car': car})

