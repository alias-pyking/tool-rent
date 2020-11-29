from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .serializers import ToolSerializer
from .models import Tool
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

User = get_user_model()


class ListCreateToolsView(ListCreateAPIView):
    serializer_class = ToolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Tool.objects.all().select_related('user').prefetch_related('images')

    def post(self, request, *args, **kwargs):
        serializer = ToolSerializer(data=request.data)
        images = request.data.getlist('images')
        serializer.is_valid(raise_exception=True)
        tool = serializer.save(user=request.user, images=images)
        serializer = ToolSerializer(instance=tool)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDeleteToolView(RetrieveUpdateDestroyAPIView):
    serializer_class = ToolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    queryset = Tool.objects.all().select_related('user')
    lookup_url_kwarg = 'tool_id'

    def put(self, request, *args, **kwargs):
        images = request.data.getlist('images')
        instance = self.get_object()
        serializer = ToolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tool = serializer.update(instance=instance, validated_data=serializer.validated_data, images=images)
        serializer = ToolSerializer(tool)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
