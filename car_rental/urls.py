# filepath: c:\project\anytime123\car_rental\urls.py
from django.urls import path
from .views import index  # Импортируем представление

urlpatterns = [
    path('', index, name='index'),  # Главная страница
]