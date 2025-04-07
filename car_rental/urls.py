from django.urls import path
from .views import index  # Импортируем представление для главной страницы
from bookings.car_views import car_list, car_detail  # Импортируем CRUD для автомобилей

urlpatterns = [
    path('', index, name='index'),  # Главная страница
    path('cars/', car_list, name='car_list'),  # Список автомобилей
    path('cars/<int:pk>/', car_detail, name='car_detail'),  # Детали автомобиля
]