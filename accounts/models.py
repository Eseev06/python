from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    driver_license = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
