from django.urls import path
from .views  import ListReviews, CreateReview


urlpatterns = [
    path('<uuid:tool_pk>/reviews/', ListReviews.as_view(), name='reviews-list'),
    path('<uuid:tool_pk>/reviews/add/', CreateReview.as_view(), name='review-add'),
]