from django.urls import path
from .views import index  # Импортируем представление для главной страницы
from car_rental.bookings.views import car_list, car_detail 


urlpatterns = [
    path('', car_list, name='index'),
    path('cars/<int:pk>/', car_detail, name='car_detail'),  # Детали автомобиля
]