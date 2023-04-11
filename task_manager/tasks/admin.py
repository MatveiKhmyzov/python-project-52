from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'executor')
    list_display_links = ('name',)
    list_filter = ('date_create',)
