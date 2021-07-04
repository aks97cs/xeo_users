# User view
from service.serializers import UserSerializer
from django.contrib.auth.models import User as uAUTH
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class User(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @staticmethod
    def get_obj(obj_id, model):
        try:
            return model.objects.get(pk=obj_id)
        except model.DoesNotExist:
            raise Http404

    def get(self, request, **kwargs):
        queryset = uAUTH.objects.all()
        _serializer = self.serializer_class(queryset, many=True)
        return Response(_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        _data = request.data
        _serializer = self.serializer_class(data=_data)
        if _serializer.is_valid():
            _serializer.save()
            return Response(_serializer.data, status=status.HTTP_201_CREATED)
        return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        user = self.get_obj(kwargs.get('id', None), uAUTH)
        _serializer = self.serializer_class(user, data=request.data)
        if _serializer.is_valid():
            _serializer.save()
            return Response(_serializer.data, status=status.HTTP_200_OK)
        return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        user = self.get_obj(kwargs.get('id', None), uAUTH)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)