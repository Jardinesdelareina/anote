from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import AnoteUser


@admin.register(AnoteUser)
class AnoteUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'phone', 'gender', 'birthday', 'is_active')
    list_display_links = ('email', 'username')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username', 'gender', 'birthday', 'avatar')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
            (None, {'fields': ('email', 'password')}),
        )
    search_fields = ('email', 'username')
    ordering = ('-date_joined',)
