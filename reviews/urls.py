from django.urls import path
from .views  import ListReviews


urlpatterns = [
    path('<uuid:tool_pk>/reivews', ListReviews.as_view(), name='reviews-list')
]