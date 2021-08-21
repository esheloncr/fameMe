from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.documentation import include_docs_urls
from .schema import CoreAPISchemaGenerator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('desc/api/', include('desktop.api.v1.urls')),
    path('auth/', include('social_django.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('doc/', include_docs_urls(title='API', authentication_classes=[], permission_classes=[],
                                   generator_class=CoreAPISchemaGenerator)),
]
