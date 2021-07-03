# Serializers
from rest_framework import serializers
from django.contrib.auth.models import User

# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )
