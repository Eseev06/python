from django.urls import path
from .views import index  # Импортируем представление для главной страницы
from car_rental.bookings.views import car_list, car_detail  # Указан полный путь к модулю

urlpatterns = [
    path('', index, name='index'),  # Главная страница
    path('cars/', car_list, name='car_list'),  # Список автомобилей
    path('cars/<int:pk>/', car_detail, name='car_detail'),  # Детали автомобиля
]