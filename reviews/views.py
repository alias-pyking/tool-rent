from tools.utils import get_tool_or_none
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .serializers import ReviewSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny


class ListCreateToolReviewsView(ListCreateAPIView):
    """
    Lists reviews of a particular tools or product.
    """
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def post(self, request, *args, **kwargs):
        user = request.user
        tool_id = kwargs['tool_id']
        tool = get_tool_or_none(tool_id)
        if tool is None:
            raise NotFound('Tool Not found')
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save(user, tool)
        serializer = ReviewSerializer(instance=review)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        tool_id = self.kwargs['tool_id']
        tool = get_tool_or_none(tool_id)
        if tool is None:
            raise NotFound('Tool not found')
        return tool.reviews.all().select_related('user')


class RetrieveToolReviewView(RetrieveAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (AllowAny, )
    lookup_url_kwarg = 'review_id'

    def get_queryset(self):
        tool_id = self.kwargs['tool_id']
        print(tool_id)
        tool = get_tool_or_none(tool_id)

        if tool is None:
            raise NotFound('Tool Not found')
        return tool.reviews.all().select_related('user')
