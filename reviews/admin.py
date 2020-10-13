from django.contrib import admin
from .models import Review



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'timestamp')

    fieldsets = (
        (None, {
            'fields':('title', 'text','user', 'tool', 'stars')
        }),
    )