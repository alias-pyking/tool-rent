from .models import Review
from rest_framework.response import Response

def get_reiview_or_none(pk):
    """
    Util to get Object of Review Model
    @param pk: pk of review
    @returns Review object or None(if not found)
    """
    try:
        review = Review.objects.get(id=str(pk))
    except:
        review = None
    return review


def review_response(review):
    """
    Util to return response for a particular Review object.
    @param review: Object of a Review model
    @returns Response Object.
    """
    return Response({
        'id':review.id,
        'user':review.user.username,
        'title':review.title,
        'text':review.title, 
        'stars':review.stars,
        'timestamp':review.timestamp
    })
