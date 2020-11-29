from django.contrib import admin
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'timestamp')

    def username(self, obj):
        return obj.user.username
