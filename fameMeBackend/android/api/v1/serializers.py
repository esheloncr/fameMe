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


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "message"
        ]


class EventSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(read_only=True, many=True)

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_login",
            "first_name",
            "last_name",
            "rating"
        ]