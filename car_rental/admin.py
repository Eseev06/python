from django.contrib import admin
from .models import CustomUser, Car, Booking, Review

admin.site.register(CustomUser)
admin.site.register(Car)
admin.site.register(Booking)
admin.site.register(Review)
