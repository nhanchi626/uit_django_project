import jwt
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import User
# Custom lại TokenObtainPairSerializer để sử dụng email thay vì username

class CustomTokenObtainSerializer(serializers.Serializer):
    userEmail = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("userEmail")
        password = attrs.get("password")

        try:
            user = User.objects.get(userEmail=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Email không tồn tại")


        if user.userPassword != password:
            raise serializers.ValidationError("Mật khẩu không đúng")

        payload = {
            'user_id': user.userID,
            'email': user.userEmail,
            'exp': datetime.utcnow() + timedelta(minutes=60), 
            'iat': datetime.utcnow()
        }       

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return {
        'access': token,
        'user': {
        'id': user.userID,
        'email': user.userEmail,
        'name': f"{user.userFirstName} {user.userLastName}",
        'role': user.userRoleID.roleName
    }
}


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'userEmail', 'userPassword', 'password2',
            'userFirstName', 'userLastName',
            'userPhone', 'userAddress', 'userRoleID'
        ]
        extra_kwargs = {
            'userPassword': {'write_only': True}
        }

    def validate(self, data):
        if data['userPassword'] != data['password2']:
            raise serializers.ValidationError("Mật khẩu không khớp.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create(**validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['userPassword']  # Exclude password field from serialization