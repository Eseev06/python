from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car_rental.urls')),  # Главная страница — список машин
    path('accounts/', include('django.contrib.auth.urls')),  # Стандартные маршруты аутентификации
    path('accounts/', include('accounts.urls')),  # Пользовательские маршруты для accounts
]

# Добавляем обработку медиафайлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)