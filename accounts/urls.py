from django.urls import path, include
from .views import register, profile, home  
urlpatterns = [
     path('', home, name='home'),
    path('register/', register, name='register'),  # Регистрация
    path('profile/', profile, name='profile'),  # Профиль пользователя
    path('', include('django.contrib.auth.urls')), 
  
]