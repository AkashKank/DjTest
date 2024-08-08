from rest_framework import serializers
from .models import Topic, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        # fields = ['id', 'user', 'topic', 'content']

class TopicSerializer(serializers.ModelSerializer):
    # messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Topic
        # fields = ['id', 'name', 'messages']
        fields = "__all__"
