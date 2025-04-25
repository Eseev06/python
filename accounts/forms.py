from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)  # Сделать необязательным
    last_name = forms.CharField(required=False)   # Сделать необязательным
    phone = forms.CharField(required=True, max_length=15, label="Телефон")

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "phone", "password1", "password2"]