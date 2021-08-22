from django.urls import path
from .views import index, bloggers, video_chat

urlpatterns = [
    path("", index),
    path("bloggers", bloggers),
    path("chat", video_chat)
]
