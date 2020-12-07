from django.urls import path
from .views import ListCreateToolTransactions

urlpatterns = [
    path('tools/<uuid:tool_id>/transactions/', ListCreateToolTransactions.as_view(),
         name='list-create-tool-transaction'),
]
