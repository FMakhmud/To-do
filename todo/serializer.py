from rest_framework import serializers
from .models import TODO


class TODOSerializer(serializers.ModelSerializer):

    class Meta:
        model = TODO
        fields = ("id", "title", "memo", "is_important", "status", "created_at", "updated_at", "user")


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, required=True)
    password = serializers.CharField(max_length=200, required=True)

