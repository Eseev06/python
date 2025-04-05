# filepath: c:\project\anytime123\car_rental\views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')