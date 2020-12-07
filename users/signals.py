from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from transactions.models import Wallet

User = get_user_model()


@receiver(post_save, sender=User)
def save_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)
