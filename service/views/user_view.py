from service.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from service.permissions import CustomHttpMethodAuthentication
from django.db import transaction
from service.utils import Utility


class User(APIView):
    serializer_class = UserSerializer
    permission_classes = [CustomHttpMethodAuthentication]
    UserModel = get_user_model()
    http_allowed_method = ['POST']

    # Get user details 
    def get(self, request, **kwargs):
        user = Utility.get_obj_by_pk(self.UserModel, kwargs.get('id', None))
        _serializer = self.serializer_class(user)
        return Response(_serializer.data, status=status.HTTP_200_OK)

    # Create user
    def post(self, request, **kwargs):
        try:
            with transaction.atomic():
                _data = request.data
                _serializer = self.serializer_class(data=_data)
                if _serializer.is_valid():
                    _serializer.save()
                    return Response(_serializer.data, status=status.HTTP_201_CREATED)
                return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

    # Update user detail
    def put(self, request, **kwargs):
        try:
            with transaction.atomic():
                user = Utility.get_obj_by_pk(self.UserModel, kwargs.get('id', None))
                _serializer = self.serializer_class(user, data=request.data, partial=True)
                if _serializer.is_valid():
                    _serializer.save()
                    return Response(_serializer.data, status=status.HTTP_200_OK)
                return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

    # Set user as in-active
    def delete(self, request, **kwargs):
        user = Utility.get_obj_by_pk(self.UserModel, kwargs.get('id', None))
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccountReactivationRequest(APIView):

    def post(self, request, **kwargs):
        pass


class PasswordResetRequest(APIView):

    def post(self, request):
        pass