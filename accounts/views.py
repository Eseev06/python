from django.shortcuts import render, redirect
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Перенаправление на главную страницу
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})