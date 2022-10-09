from django import forms
from django.forms import ModelForm
from .models import AnoteUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class AccountForm(ModelForm):
    class Meta:
        model = AnoteUser
        fields = ['username', 'phone', 'gender', 'avatar', 'birthday']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Имя пользователя'
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'input',
                'placeholder': 'Номер телефона'
            }),
            'gender': forms.Select(attrs={
                'class': 'select'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'file',
                'placeholder': 'Загрузить'
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'date'
            }),
        }


class AnoteUserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = AnoteUser
        fields = ['email', 'password1', 'password2']


class AnoteUserAuthForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))
