from rest_framework import serializers
from django.contrib.auth.models import User
from .models import employee_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')  # Includes all fields in JSON response

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')  # Includes all fields in JSON response
    def create(self, validated_data):
        user = User.objects.create_user(
        validated_data['username'],
        validated_data['email'],
        validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True , write_only = True)