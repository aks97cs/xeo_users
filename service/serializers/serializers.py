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
    info = UserInoSerializer()

    def validate_password(self, password):
        # validating password
        if not password:
            raise serializers.ValidationError('Invalid request')

        if not len(password) == self.PASSWORD_LENGTH:
            raise serializers.ValidationError('Password length should be 5')
        return password

    def create(self, validated_data):
        """
        Create new user and return user instance
        """
        info = validated_data.pop('info')
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        UserInfo.objects.create(user=user, **info)
        return user
    
    def update(self, user, validated_data):
        """
        Updating user data and return user instance
        """
        info = validated_data.pop('info')
        # Updating user data
        user.username = validated_data.get('username', user.username)
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.save()

        # Updating/Creating user info data
        info_instance = None
        if hasattr(user, 'info'):
            info_instance = user.info
        else:
            info_instance = UserInfo()
        info_instance.address = info.get('address', info_instance.address)
        info_instance.user = user
        info_instance.save()
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
            'password': {'write_only': True},
        }
