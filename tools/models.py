import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

def upload_to_aws_s3(instance):
    """
    Upload images to s3 or azure static storage bucket
    TODO: Will be imlemented later (after we buy s3 or azure static storage obviously )
    """
    pass

class Picture(models.Model):
    """
    Purpose: This model will be used by other models for adding images
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    image_alt_text = models.CharField('Alt Text for image', max_length=50)
    image = models.ImageField("Picture", upload_to=upload_to_aws_s3)
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
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tool-detail', kwargs={'pk':self.id})    
    
    def get_reviews_url(self):
        return reverse('reviews-list', kwargs={'tool_pk':self.id})
