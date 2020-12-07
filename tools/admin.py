from django.contrib import admin
from .models import Tool, Picture


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'name', 'cost_per_day', 'quantity', 'status', 'timestamp'

    fieldsets = (
        (None, {
            'fields': ('name', 'user', 'images', 'description', 'status', 'quantity', 'cost_per_day')
        }),
    )


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_alt_text', 'timestamp')
