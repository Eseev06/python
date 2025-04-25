from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Car, Booking, Review



# Кастомная модель пользователя
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'driver_license')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'phone', 'driver_license')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'email', 'phone', 'driver_license', 'address')}),
        ('Права', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2'),
        }),
    )

# Модель автомобиля
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'price_per_day', 'city', 'status']  # Добавляем статус в список
    list_editable = ['price_per_day', 'city', 'status']  # Делаем статус редактируемым
    list_filter = ('brand', 'year', 'transmission', 'seats', 'city', 'status')  # Добавляем фильтр по статусу
    search_fields = ('brand', 'name', 'city')  # Поиск по полям
    readonly_fields = ('image_preview',)
    fieldsets = (
        (None, {
            'fields': ('brand', 'name', 'year', 'city', 'status')  # Добавляем статус в секцию
        }),
        ('Технические характеристики', {
            'fields': ('transmission', 'seats', 'price_per_day')
        }),
        ('Изображение', {
            'fields': ('image', 'image_preview')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 150px;" />', obj.image.url)
        return "Нет изображения"
    image_preview.short_description = 'Превью'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 150px;" />', obj.image.url)
        return "Нет изображения"
    image_preview.short_description = 'Превью'

    def price_formatted(self, obj):
        return f"${obj.price_per_day}/день"
    price_formatted.short_description = 'Цена'

    def transmission_display(self, obj):
        return dict(Car.TRANSMISSION_CHOICES).get(obj.transmission)
    transmission_display.short_description = 'Коробка'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 150px;" />', obj.image.url)
        return "Нет изображения"
    image_preview.short_description = 'Превью'
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'rating_stars', 'short_comment', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'car__brand', 'car__name', 'comment')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('user', 'car', 'rating')
        }),
        ('Содержание', {
            'fields': ('comment', 'created_at')
        }),
    )

    def rating_stars(self, obj):
        return format_html(
            '{} ★',
            obj.rating
        )
    rating_stars.short_description = 'Рейтинг'

    def short_comment(self, obj):
        max_len = 60
        if len(obj.comment) > max_len:
            return f"{obj.comment[:max_len]}..."
        return obj.comment
    short_comment.short_description = 'Комментарий'