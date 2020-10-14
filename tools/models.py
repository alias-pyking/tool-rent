import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import os


User = get_user_model()

def upload_to_aws_s3(instance, filename):
    """
    Upload images in media/tools/ dir in s3 bucket
    """
    return 'tools/'+ filename
    
class Picture(models.Model):
    """
    Purpose: This model will be used by other models for adding images
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    image_alt_text = models.CharField('Alt Text for image', max_length=50)
    image = models.ImageField("Picture", upload_to=upload_to_aws_s3, null=True, blank=True, help_text=_('Add Image'))
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.image_alt_text)

class Tool(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name of Tool', max_length=50)
    description = models.TextField(verbose_name='Description')
    quantity = models.IntegerField(verbose_name='Quantity', help_text='How many of these you have ?', null=True, blank=True)
    cost = models.DecimalField(verbose_name='Price of the Tool',max_digits=10, decimal_places=4)
    status = models.BooleanField('Status', help_text=_('Is this tool available right now or not ?'), default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tool-detail', kwargs={'pk':self.id})    
    
    def get_reviews_url(self):
        return reverse('reviews-list', kwargs={'tool_pk':self.id})
