from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import AnoteUser


@admin.register(AnoteUser)
class AnoteUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'display_name', 'phone', 'gender', 'birthday', 'is_active')
    list_display_links = ('email', 'display_name')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone')}),
        (_('Personal info'), {'fields': ('display_name', 'gender', 'birthday', 'avatar')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active')}),
    )
    search_fields = ('email', 'display_name')
    ordering = ('-date_joined',)
