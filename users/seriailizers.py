from rest_framework import serializers
from .models import User
from transactions.serializers import WalletSerializer


class ProfileSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ('is_staff', 'is_superuser', 'is_active', 'password', 'groups', 'user_permissions')


