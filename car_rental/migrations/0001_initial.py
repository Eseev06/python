# Generated by Django 5.2 on 2025-04-19 14:33

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('brand', models.CharField(max_length=100, verbose_name='Марка')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за день')),
                ('transmission', models.CharField(choices=[('manual', 'Механическая'), ('automatic', 'Автоматическая')], default='automatic', max_length=10, verbose_name='Коробка передач')),
                ('seats', models.PositiveIntegerField(default=5, verbose_name='Количество мест')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('status', models.CharField(choices=[('pending', 'Ожидание'), ('confirmed', 'Подтверждено'), ('canceled', 'Отменено'), ('completed', 'Завершено')], default='pending', max_length=10, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental.car', verbose_name='Автомобиль')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Рейтинг')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental.car', verbose_name='Автомобиль')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
