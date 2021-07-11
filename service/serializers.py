# Serializers
from rest_framework import serializers
from django.contrib.auth import get_user_model
from service.models import UserInfo


# UserInfo Serializer
class UserInoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('address', )


# user serializer
class UserSerializer(serializers.ModelSerializer):
    PASSWORD_LENGTH = 5

    def validate_password(self, password):
        # validating password
        if not password:
            raise serializers.ValidationError('Invalid request')

        if not len(password) == self.PASSWORD_LENGTH:
            raise serializers.ValidationError('Password length should be 5')
        return password

    def create(self, validated_data):
        info_data = validated_data.pop('info')
        user = self.Meta.model(**validated_data)
        user.set_password(validated_data['password'])
        _u = user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
            'is_active',
            'is_staff',
            'first_name',
            'last_name',
            'is_superuser',
            'info',
            'password',
        )
        read_only_fields = ('is_active', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    info = UserInoSerializer()






