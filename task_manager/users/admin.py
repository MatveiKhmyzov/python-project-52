from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_active')
    list_display_links = ('username',)
    list_editable = ('is_active',)
    list_filter = ('date_joined', 'is_active')
