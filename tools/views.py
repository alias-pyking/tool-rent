from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework import permissions
from .serializers import ListToolSerializer, CreateUpdateToolSerializer
from .models import Tool
from rest_framework.response import Response
from .utils import get_tool_or_none, tool_response
from rest_framework import status
from .permissions import IsAuthorOrReadOnly

User = get_user_model()

"""
TODO: Adding permission and authentication classes to all these views.
"""


class ListTools(ListAPIView):
    serializer_class = ListToolSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Tool.objects.all()


class ToolDetail(RetrieveAPIView):
    serializer_class = ListToolSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Tool.objects.all()


class DeleteTool(DestroyAPIView):
    serializer_class = ListToolSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Tool.objects.all()


class EditTool(UpdateAPIView):
    serializer_class = CreateUpdateToolSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = CreateUpdateToolSerializer(data=request.data)
        images = request.data.getlist('images')
        if images is None or images[0] != '':
            images = None
        if serializer.is_valid(raise_exception=True):
            tool_pk = kwargs['pk']
            tool = get_tool_or_none(pk=tool_pk)
            if tool:
                tool = serializer.update(tool, serializer.validated_data, images=images)
                return tool_response(tool)
            else:
                return Response(data={"detail": "Tool not found"}, status=status.HTTP_404_NOT_FOUND)


class CreateTool(CreateAPIView):
    serializer_class = CreateUpdateToolSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateUpdateToolSerializer(data=request.data)
        images = request.data.getlist('images')

        if images is None or images[0] == '':
            return Response(data=[{'images': 'This field is required'}])

        if serializer.is_valid(raise_exception=True):
            tool = serializer.save(user=User.objects.get(id=1), images=images)
            return tool_response(tool)
