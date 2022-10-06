from asyncore import read
from rest_framework import serializers
from .models import User, Thread, ChatMessage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ThreadSerializer(serializers.ModelSerializer):
    user_from = UserSerializer(read_only=True)
    user_to = UserSerializer(read_only=True)
    class Meta:
        model = Thread
        fields = ('id', 'user_from', 'user_to', 'is_opened_from', 'is_opened_to', 'created_at', 'updated_at')

class ChatMessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ChatMessage
        fields = ('id', 'thread', 'user', 'message', 'is_read', 'created_at', 'updated_at')