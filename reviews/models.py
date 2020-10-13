from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
import uuid
from tools.models import Tool
from django.urls import reverse
from django.core.exceptions import ValidationError


User = get_user_model()


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    title = models.CharField('Review Title', max_length=50, help_text=_('Determines type of review for tool: Good, Bad, Great... '))
    text = models.TextField('Review Description', help_text=_('Description of review'))
    stars = models.IntegerField('Stars', help_text=_('How will you rate this tool out of 5'), null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.title)
    
    def clean(self):
        error_messages = {}
        if self.stars is None or self.stars == '':
            error_messages.update({
                'stars':'Stars field cannot be empty'
            })
        elif self.stars > 5:
            error_messages.update({
                'stars':'Stars cannot have maximum 5 value'
            })
        
        if error_messages:
            raise ValidationError(error_messages)

