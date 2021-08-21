from django.urls import path
from .views import dev, vk_login, inst_login, get_event, like, comment, get_user, BloggersViewSet, PeopleViewSet, \
    EventRegister, EventApiView
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from fameMeBackend.schema import CoreAPISchemaGenerator

router = routers.SimpleRouter()
router.register(r"bloggers_list", BloggersViewSet)
router.register(r"people_list", PeopleViewSet)
router.register(r"new_event", EventRegister)
router.register(r"events", EventApiView)


urlpatterns = router.urls + [
    path("dev/", dev, name="dev"),
    path("vk_login", vk_login, name="vk"),
    path("inst_login", inst_login, name="inst"),
    path("event/<int:pk>", get_event, name="event"),
    path("like/<int:pk>", like, name="like"),
    path("comment/<int:pk>", comment),
    path("user/<int:pk>", get_user),
    path('doc/', include_docs_urls(title='API', authentication_classes=[], permission_classes=[],
                                         generator_class=CoreAPISchemaGenerator)),
]
