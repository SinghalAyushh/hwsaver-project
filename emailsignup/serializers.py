from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
   
    def validate(self, data):
        email = authenticate(**data)
        if email and email.is_active:
            return email
        raise serializers.ValidationError("Unable to log in with provided credentials.")        