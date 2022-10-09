from django.shortcuts import render, redirect
from .forms import AnoteUserRegisterForm, AnoteUserAuthForm
from .models import AnoteUser
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import DetailView


class AccountDetailView(DetailView):
    model = AnoteUser
    template_name = 'account/profile.html'
    context_object_name = 'profile_view'

def register(request):
    if request.method == 'POST':
        form = AnoteUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешно завершена')
            return redirect('profile/<int:pk>')
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
            return redirect('profile/<int:pk>')
    else:
        form = AnoteUserAuthForm()
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')
