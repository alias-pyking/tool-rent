from django.urls import path
from .views import DetailUpdateProfileView

urlpatterns = [
    path('profile/<str:username>/', DetailUpdateProfileView.as_view(), name='profile')
]

