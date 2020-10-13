from rest_framework.generics import ListAPIView
from .serializers import ReviewSerializer
from tools.utils import get_tool_or_none
from rest_framework.response import Response
from rest_framework import status


class ListReviews(ListAPIView):
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
            return Response(data={'detail':'Tool Not found'}, status=status.HTTP_404_NOT_FOUND)
        






