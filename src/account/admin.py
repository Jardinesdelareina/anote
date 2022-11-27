from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'is_active')
    list_display_links = ('email', 'username')
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        (_('Personal info'), {'fields': ('about', 'avatar')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active')}),
    )
    search_fields = ('email', 'username')
    ordering = ('-date_joined',)
