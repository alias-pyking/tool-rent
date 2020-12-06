from rest_framework import serializers
from .models import User


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('is_staff', 'is_superuser', 'is_active', 'password', 'groups', 'user_permissions')

