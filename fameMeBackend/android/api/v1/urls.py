from django.urls import path
from .views import dev, vk_login, inst_login

urlpatterns = [
    path("dev/", dev),
    path("vk_login", vk_login),
    path("inst_login", inst_login),
]