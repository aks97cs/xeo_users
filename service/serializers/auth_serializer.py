from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AuthSerializer(TokenObtainPairSerializer):

    username_field = 'username'

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
