from django.urls import path
from .views import ListTools, ToolDetail, CreateTool, DeleteTool, EditTool


urlpatterns = [
    path('', ListTools.as_view(), name='tools-list'),
    path('add/', CreateTool.as_view(), name='tool-add'),
    path('<uuid:pk>/', ToolDetail.as_view(), name='tool-detail'),
    path('<uuid:pk>/edit/', EditTool.as_view(), name='tool-edit'),
    path('<uuid:pk>/delete/', DeleteTool.as_view(), name='tool-delete'),
]