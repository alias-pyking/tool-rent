from rest_framework import serializers
from .models import Transaction, Wallet
from tools.serializers import ToolSerializer

"""
TODO: Complete transaction with payment,
TODO: Credit the seller account with the money as per transaction, 
TODO: Invalidate the transaction if expiration time is over
TODO: Implement APIs for user transactions things which he have bought
TODO: Implement APIs for user transactions things which he have sold
"""


class TransactionSerializer(serializers.ModelSerializer):
    buyer = serializers.SerializerMethodField()
    seller = serializers.SerializerMethodField()
    tool = ToolSerializer(read_only=True)
    payment_status = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    cost = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=10)
    selling_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'

    def save(self, **kwargs):
        buyer = kwargs['user']
        tool = kwargs['tool']
        seller = tool.user
        transaction = Transaction.objects.create(buyer=buyer, seller=seller, tool=tool, payment_status='not_completed',
                                                 cost_per_hour=tool.cost_per_hour, status='ongoing',
                                                 **self.validated_data)
        return transaction

    @staticmethod
    def get_buyer(obj):
        return obj.buyer.username

    @staticmethod
    def get_seller(obj):
        return obj.seller.username


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        exclude = ('user',)


class StripUserInfoSerializer(serializers.Serializer):
    email = serializers.EmailField()
    payment_method_id = serializers.CharField()

    def create(self, validated_data):
        pass

    def save(self, **kwargs):
        pass

    def update(self, instance, validated_data):
        pass
