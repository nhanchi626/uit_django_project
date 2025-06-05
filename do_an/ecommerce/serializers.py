from rest_framework import serializers
from .models import User

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