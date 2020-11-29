from django.urls import path
from .views import ListCreateToolsView, RetrieveUpdateDeleteToolView

urlpatterns = [
    path('', ListCreateToolsView.as_view(), name='list-create-tools'),
    path('<uuid:tool_id>/', RetrieveUpdateDeleteToolView.as_view(), name='get-update-delete-tool')
]
