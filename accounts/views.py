from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegisterForm  # Создайте этот файл, как в предыдущем ответе

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Или другой целевой URL
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    return render(request, 'accounts/profile.html')