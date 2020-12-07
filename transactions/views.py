from rest_framework.response import Response
from .serializers import TransactionSerializer, StripUserInfoSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from tools.utils import ensure_tool
from django.conf import settings
from .utils import get_transaction_or_none
from rest_framework.exceptions import NotFound
from django.utils.timezone import now
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_cost(starting_time, expiration_time, cost_per_hour):
    cost = ((expiration_time.day - starting_time.day)*24 + (24 - starting_time.hour) + expiration_time.hour)
    cost = float(cost*cost_per_hour)
    return cost


class ListCreateToolTransactions(ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )

    @ensure_tool
    def get_queryset(self):
        tool = self.kwargs['tool']
        return tool.transactions.all().select_related('buyer', 'seller')

    @ensure_tool
    def post(self, request, *args, **kwargs):
        tool = self.kwargs['tool']
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tool = serializer.save(tool=tool, user=request.user)
        serializer = TransactionSerializer(instance=tool)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ToolPayment(APIView):
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = StripUserInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = data['email']
        payment_method_id = data['payment_method_id']
        customer_data = stripe.Customer.list(email=email).data

        if len(customer_data) == 0:
            customer = stripe.Customer.create(
                email=email, payment_method=payment_method_id)
        else:
            customer = customer_data[0]

        transaction_id = self.kwargs['transaction_id']
        transaction = get_transaction_or_none(transaction_id)
        if transaction is None:
            raise NotFound('Transaction Not found')
        cost_per_hour = transaction.cost_per_hour
        starting_time = now()
        expiration_time = transaction.expiration_time
        transaction.selling_time = starting_time
        transaction.cost = get_cost(starting_time, expiration_time, cost_per_hour)
        transaction.payment_status = 'completed'
        transaction.save()
        seller = transaction.seller
        seller_wallet = seller.wallet
        seller_wallet.money = float(seller_wallet.money) + transaction.cost
        seller_wallet.save()
        test_payment_intent = stripe.PaymentIntent.create(
            amount=int(transaction.cost*100), currency='inr',
            customer=customer, payment_method=payment_method_id
            )
        return Response(data=test_payment_intent, status=status.HTTP_200_OK)


class SaveStripeUserInfo(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = StripUserInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = data['email']
        payment_method_id = data['payment_method_id']
        customer_data = stripe.Customer.list(email=email).data

        if len(customer_data) == 0:
            customer = stripe.Customer.create(
                email=email, payment_method=payment_method_id)
        else:
            customer = customer_data[0]

        return Response(
            data={'message': 'Success', 'data': {'customer_id': customer.id}},
            status=status.HTTP_200_OK
        )
