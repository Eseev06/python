from django.urls import path
from .views import index, my_bookings, faq  # Импортируем представление для FAQ
from car_rental.bookings.views import car_list, car_detail

urlpatterns = [
    path('', car_list, name='index'),  # Главная страница
    path('cars/<int:pk>/', car_detail, name='car_detail'),  # Детали автомобиля
    path('my-bookings/', my_bookings, name='my_bookings'),  # Мои бронирования
    path('faq/', faq, name='faq'),  # Вопрос-Ответ
]