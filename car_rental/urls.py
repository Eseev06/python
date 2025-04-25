from django.urls import path
from .views import index, my_bookings, faq
from car_rental.bookings.views import car_list, car_detail  # car_list и car_detail из другой view

urlpatterns = [
    path('', index, name='index'),  # Главная страница теперь использует представление index
    path('cars/<int:pk>/', car_detail, name='car_detail'),  # Детали автомобиля
    path('my-bookings/', my_bookings, name='my_bookings'),  # Мои бронирования
    path('faq/', faq, name='faq'),  # Вопрос-Ответ
]
