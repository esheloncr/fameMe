from rest_framework import serializers
from android.models import Event, Comment, User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "followers",
            "is_blogger",
            "event_counter"
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'author',
            'description',
            'like',
            'liked_by',
            'comments',
        ]


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'author',
            'description'
        ]