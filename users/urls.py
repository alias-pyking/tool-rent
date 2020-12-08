from django.urls import path
from .views import DetailUpdateProfileView, UserTools, UserTransactions

urlpatterns = [
    path('profile/<str:username>/', DetailUpdateProfileView.as_view(), name='profile'),
    path('profile/<str:username>/tools/', UserTools.as_view(), name='user-tools'),
    path('profile/<str:username>/transactions/', UserTransactions.as_view(), name='user-transactions')
]

