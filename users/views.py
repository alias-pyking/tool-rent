from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.account.views import ConfirmEmailView
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.shortcuts import redirect
from rest_framework.views import APIView
from dj_rest_auth.registration.serializers import VerifyEmailSerializer
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import AllowAny
from django.utils.translation import ugettext_lazy as _
from rest_framework import status

class VerifyEmailView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        key = kwargs['key']
        data = {
            'key':key
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'detail': _('ok'), 'message':_('Confirmed')}, status=status.HTTP_200_OK)

# class RegisterAPIView(APIView):
#     methods = 
#     def post(self, request, *args, **kwargs):
