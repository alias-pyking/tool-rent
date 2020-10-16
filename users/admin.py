from django.contrib import admin
from .models import Profile, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'timestamp')

    def username(self, obj):
        return obj.user.username
