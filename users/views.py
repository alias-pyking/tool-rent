from rest_framework.response import Response
from allauth.account.views import ConfirmEmailView
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from dj_rest_auth.registration.serializers import VerifyEmailSerializer
from rest_framework.permissions import AllowAny
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSelfOrReadOnly
from .models import User
from .seriailizers import ProfileSerializer


class VerifyEmailView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'OPTIONS', 'HEAD')

    @staticmethod
    def get_serializer(*args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        key = kwargs['key']
        data = {
            'key': key
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'detail': _('ok'), 'message': _('Confirmed')}, status=status.HTTP_200_OK)


class DetailUpdateProfileView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsSelfOrReadOnly)
    queryset = User.objects.all().select_related('wallet')
    lookup_field = 'username'
    serializer_class = ProfileSerializer
