from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            print(f"Пользователь {user.username} вошел в систему")  # Отладка
            return redirect('profile')  # Перенаправление на страницу профиля
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')  # Отображаем страницу профиля
@login_required
def home(request):
    return render(request, 'accounts/home.html', {'user': request.user})