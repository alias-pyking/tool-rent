from django.contrib import admin
from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'name', 'cost', 'quantity', 'timestamp'

    fieldsets = (
        (None, {
            'fields': ('name', 'user', 'description', 'quantity', 'cost')
        }),
    )