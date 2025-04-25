from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    driver_license = models.CharField(max_length=50, blank=True, verbose_name="Водительское удостоверение")
    address = models.TextField(blank=True, verbose_name="Адрес")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'