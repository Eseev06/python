from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('', include('car_rental.urls')),  # Подключение маршрутов приложения car_rental
]