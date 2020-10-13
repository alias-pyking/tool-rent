
from tools.utils import get_tool_or_none
from rest_framework.response import Response
from rest_framework import status

from .serializers import ReviewSerializer, CreateReviewSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from .utils import review_response

class ListReviews(ListAPIView):
    """
    Lists reviews of a particular tools or product.
    TODO: Add authentication and permissions classes
    """
    serializer_class = ReviewSerializer
    queryset = []

    def get(self, request, *args, **kwargs):
        tool_pk = str(kwargs['tool_pk'])
        tool = get_tool_or_none(pk=tool_pk)
        if tool:
            queryset = tool.review_set.all()
            serializer = ReviewSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail':'Tool with id {} not found'.format(tool_pk)}, status=status.HTTP_404_NOT_FOUND)

class CreateReview(CreateAPIView):
    """
    Creates a review for a partiuclar product
    TODO: Add Authentication and permission classes(Will have to write one)
    """
    serializer_class = CreateReviewSerializer

    def post(self, request, *args, **kwargs):
        tool_pk = str(kwargs['tool_pk'])
        tool = get_tool_or_none(pk=tool_pk)
        if tool:
            serializer = CreateReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                review = serializer.save(user=request.user, tool=tool)
                return review_response(review)
        else:
            return Response(data={'detail':'Tool with id {} not found'.format(tool_pk)})


        






