from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User

        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'role'
        )

        read_only_fields = ('id', 'role')

    def create(self, validated_data):

        password = validated_data.pop('password')

        user = User.objects.create_user(
            password=password,
            role=User.Role.PATIENT,
            **validated_data
        )

        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'role'
        )

        read_only_fields = ('id', 'username', 'role')


class StaffCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'role',
        )

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        return user        