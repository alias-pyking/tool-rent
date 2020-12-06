from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    buyer = serializers.SerializerMethodField()
    seller = serializers.SerializerMethodField()
    tool = serializers.SerializerMethodField()
    payment_status = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    cost = serializers.DecimalField(read_only=True, decimal_places=4, max_digits=10)

    class Meta:
        model = Transaction
        fields = '__all__'

    def save(self, **kwargs):
        buyer = kwargs['user']
        tool = kwargs['tool']
        seller = tool.user
        transaction = Transaction.objects.create(buyer=buyer, seller=seller, tool=tool, payment_status='not_completed',
                                                 cost=tool.cost, status='on_going', **self.validated_data)
        return transaction

    @staticmethod
    def get_buyer(obj):
        return obj.buyer.username

    @staticmethod
    def get_seller(obj):
        return obj.seller.username
