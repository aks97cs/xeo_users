from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class Auth(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # token value: (<Token: a018aec7c5476ef8382c7a2803c64f4bb9432453>, False)
        token = Token.objects.get_or_create(user=user)
        return Response({
            'token': token[0].key,
            'user_id': user.pk,
            'email': user.email
        })
