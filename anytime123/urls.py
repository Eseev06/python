from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views  # Импорт встроенных представлений аутентификации

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('', include('car_rental.urls')),  # Подключение маршрутов приложения car_rental
    
    # Добавляем маршруты для аутентификации
    path('accounts/', include('django.contrib.auth.urls')),  # Встроенные auth URLs (login, logout, password change и т.д.)
    path('accounts/', include('accounts.urls')),  # Ваши кастомные URLs для аккаунтов
]