from django.contrib import admin

from .models import CustomUser

from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'telegram', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
