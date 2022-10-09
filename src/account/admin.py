from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import AnoteUser


@admin.register(AnoteUser)
class AnoteUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'gender', 'birthday', 'is_active')
    list_display_links = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone')}),
        (_('Personal info'), {'fields': ('gender', 'birthday', 'avatar')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active')}),
    )
    search_fields = ('username', 'email')
    ordering = ('date_joined',)
