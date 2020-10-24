from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


# User = get_user_model()

class User(AbstractUser):
    pass


class Profile(models.Model):
    """
    This model is linked with User using OneToOneRelation and is used to add other info
    like bio, profile image to a user account
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('User Profile Pic', default='img/default_profile.jpg')
    bio = models.TextField("User Bio", help_text=_('Small description about user in 500 characters'), max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.user.username)
