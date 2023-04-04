from django.contrib import admin
from .models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    list_filter = ('date_create',)
