from django.urls import path
from .views import DetailUpdateProfileView, UserTools

urlpatterns = [
    path('profile/<str:username>/', DetailUpdateProfileView.as_view(), name='profile'),
    path('profile/<str:username>/tools/', UserTools.as_view(), name='user-tools'),
]

