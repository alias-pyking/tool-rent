from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from tools.models import Tool
import uuid

User = get_user_model()

TRANSACTION_PAYMENT_CHOICES = (
    ('not_completed', 'Not Completed'),
    ('partially_completed', 'Partially Completed'),
    ('completed', 'Completed')
)

TRANSACTION_STATUS_CHOICES = (
    ('ongoing', 'On Going'),
    ('expired', 'Expired'),
)


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    buyer = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='tools_bought')
    seller = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='tools_sold')
    tool = models.ForeignKey(to=Tool, on_delete=models.SET_NULL, null=True, related_name='transactions')
    selling_time = models.DateTimeField('When transaction is made', default=now)
    expiration_time = models.DateTimeField('When will this transaction expire')
    payment_status = models.CharField('Payment Status', null=True, choices=TRANSACTION_PAYMENT_CHOICES, max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    status = models.CharField('Status', null=True, choices=TRANSACTION_STATUS_CHOICES, max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
