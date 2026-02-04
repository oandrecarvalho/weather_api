from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'city', 'state')
        extra_kwargs = {'password': {'write_only': True}}

def create_user(data):
    user = User.objects.create_user(**validated_data)
    return user