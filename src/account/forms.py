from django import forms
from .models import AnoteUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class AnoteUserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = AnoteUser
        fields = ['email', 'password1', 'password2']


class AnoteUserAuthForm(AuthenticationForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))
