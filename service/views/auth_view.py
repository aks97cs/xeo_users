from service.serializers import AuthSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status


class Auth(APIView):
    serializer_class = AuthSerializer

    def post(self, request):

        user = authenticate(**request.data)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        response = serializer.validated_data
        response.update(
            {
                'username': user.username,
                'id': user.id
            }
        )
        return Response(response, status=status.HTTP_200_OK)
