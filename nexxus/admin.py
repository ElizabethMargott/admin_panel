from django.contrib import admin
from django.shortcuts import render
import requests
from .models import User
from django.utils import timezone
from datetime import timedelta

# Define tus acciones personalizadas primero
@admin.action(description='Suspender usuarios seleccionados por 30 días')
def suspend_users(modeladmin, request, queryset):
    for user in queryset:
        user.is_suspended = True
        user.suspended_until = timezone.now() + timedelta(days=30)
        user.save()

@admin.action(description='Levantar suspensión de usuarios seleccionados')
def unsuspend_users(modeladmin, request, queryset):
    for user in queryset:
        user.is_suspended = False
        user.suspended_until = None
        user.save()

# Define tu clase UserAdmin
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_suspended', 'suspended_until']
    actions = [suspend_users, unsuspend_users]

# Comprueba si el modelo User ya está registrado antes de intentar desregistrarlo
if User in admin.site._registry:
    admin.site.unregister(User)

# Registra el modelo User con la configuración personalizada de UserAdmin
admin.site.register(User, UserAdmin)
