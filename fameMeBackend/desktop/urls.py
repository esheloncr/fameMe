from django.urls import path
from .views import index, bloggers

urlpatterns = [
    path("", index),
    path("bloggers", bloggers)
]