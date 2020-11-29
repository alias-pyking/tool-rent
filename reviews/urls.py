from django.urls import path
from .views import ListCreateToolReviewsView, RetrieveToolReviewView


urlpatterns = [
    path('<uuid:tool_id>/reviews/', ListCreateToolReviewsView.as_view(), name='reviews-list'),
    path('<uuid:tool_id>/reviews/<uuid:review_id>/', RetrieveToolReviewView.as_view(), name='detail-review'),
]
