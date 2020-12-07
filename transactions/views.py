from rest_framework.response import Response
from .serializers import TransactionSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from tools.utils import ensure_tool


class ListCreateToolTransactions(ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )

    @ensure_tool
    def get_queryset(self):
        tool = self.kwargs['tool']
        return tool.transactions.all().select_related('buyer', 'seller')

    @ensure_tool
    def post(self, request, *args, **kwargs):
        tool = self.kwargs['tool']
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tool = serializer.save(tool=tool, user=request.user)
        serializer = TransactionSerializer(instance=tool)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
