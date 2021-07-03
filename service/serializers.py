# Serializers
from rest_framework import serializers
from django.contrib.auth import get_user_model

# user serializer
class UserSerializer(serializers.ModelSerializer):
    PASSWORD_LENGHT = 5
    def validate_password(self, password):
        # validating password
        if not password:
            raise serializers.ValidationError('Invalid request')
        
        if not len(password) == self.PASSWORD_LENGHT:
            raise serializers.ValidationError('Password length should be 5')
        return password


    
    def create(self, validated_data):
        user = self.Meta.model(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = get_user_model()
        fields = '__all__'
    
