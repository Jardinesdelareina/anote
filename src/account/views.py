from django.shortcuts import render, redirect
from .forms import AnoteUserRegisterForm, AnoteUserAuthForm
from django.contrib.auth import login, logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = AnoteUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешно завершена')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при регистрации')
    else:
        form = AnoteUserRegisterForm()    
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = AnoteUserAuthForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AnoteUserAuthForm()
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')
