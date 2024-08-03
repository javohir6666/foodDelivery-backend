from rest_framework import serializers
from .models import CustomUser

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])
        data['access'] = str(refresh.access_token)
        return data