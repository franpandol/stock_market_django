from django.db import IntegrityError
from rest_framework import serializers

from authentication.models import Account


class UserCreateSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(read_only=True)

    default_error_messages = {"cannot_create_user": "Error creating user"}

    class Meta:
        model = Account

        fields = tuple(Account.REQUIRED_FIELDS) + (
            "name",
            "last_name",
            "email",
            "auth_token",
        )

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")
        return user

    def perform_create(self, validated_data):
        user = Account.objects.create(**validated_data)
        return user
