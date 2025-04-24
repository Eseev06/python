from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import CustomUser

# class CustomUser(AbstractUser):
#     phone = models.CharField(max_length=20, blank=True)
#     driver_license = models.CharField(max_length=50, blank=True)
#     address = models.TextField(blank=True)
    
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('manual', 'Механическая'),
        ('automatic', 'Автоматическая'),
    ]

    CITY_CHOICES = [
        ('Алматы', 'Алматы'),
        ('Нур-Султан', 'Нур-Султан'),
        ('Шымкент', 'Шымкент'),
        ('Караганда', 'Караганда'),
        ('Актобе', 'Актобе'),
    ]
    city = models.CharField(
        max_length=100,
        choices=CITY_CHOICES,
        verbose_name='Город',
        default='Алматы'
    )

    name = models.CharField(max_length=100, verbose_name='Название')
    brand = models.CharField(max_length=100, verbose_name='Марка')
    year = models.IntegerField(verbose_name='Год выпуска')
    price_per_day = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='Цена за день'
    )
    transmission = models.CharField(
        max_length=10,
        choices=TRANSMISSION_CHOICES,
        default='automatic',
        verbose_name='Коробка передач'
    )
    seats = models.PositiveIntegerField(default=5, verbose_name='Количество мест')
    
    image = models.ImageField(upload_to='cars/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return f"{self.brand} {self.name} ({self.year})"
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('confirmed', 'Подтверждено'),
        ('canceled', 'Отменено'),
        ('completed', 'Завершено'),
    ]
    
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    car = models.ForeignKey(
        Car, 
        on_delete=models.CASCADE,
        verbose_name='Автомобиль'
    )
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.user.username} - {self.car} ({self.status})"
    def clean(self):
        # Проверяем пересечение дат
        overlapping_bookings = Booking.objects.filter(
            car=self.car,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        ).exclude(pk=self.pk)
        if overlapping_bookings.exists():
            raise ValidationError('На выбранные даты машина уже забронирована.')

class Review(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    car = models.ForeignKey(
        Car, 
        on_delete=models.CASCADE,
        verbose_name='Автомобиль'
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Рейтинг'
    )
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.user.username} - {self.car} ({self.rating}/5)"