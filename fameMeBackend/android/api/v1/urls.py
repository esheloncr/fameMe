from django.urls import path
from .views import dev, vk_login, inst_login, get_event, like, BloggersViewSet, PeopleViewSet, EventRegister
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"bloggers_list", BloggersViewSet)
router.register(r"people_list", PeopleViewSet)
router.register(r"new_event", EventRegister)

urlpatterns = router.urls + [
    path("dev/", dev),
    path("vk_login", vk_login),
    path("inst_login", inst_login),
    path("event/<int:pk>", get_event),
    path("like/<int:pk>", like)
]