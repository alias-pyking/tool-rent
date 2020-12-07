from django.urls import path
from .views import ListCreateToolTransactions, ToolPayment, SaveStripeUserInfo

urlpatterns = [
    path('tools/<uuid:tool_id>/transactions/', ListCreateToolTransactions.as_view(),
         name='list-create-tool-transaction'),
    path('transactions/<uuid:transaction_id>/pay/', ToolPayment.as_view(), name='transaction-payment'),
    path('transactions/save_stripe_user_info/', SaveStripeUserInfo.as_view(), name='save-stripe-user-info'),
]
