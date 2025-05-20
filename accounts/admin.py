from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('role', 'email_confirmed')}),
    )
    list_display = ['username', 'email', 'role', 'email_confirmed']

admin.site.register(CustomUser, CustomUserAdmin)