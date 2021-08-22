from django.contrib import admin
from .models import Event, Comment, User, Image
# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        "image"
    ]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'followers',
        'event_counter',
        'is_blogger',
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        self.exclude = (
            'is_active',
            'is_admin',
            'is_staff',
            'email',
            'groups',
            'password',
            'user_permissions',
            'is_superuser',
            'date_joined',
            'last_login'
        )
        form = super(UserAdmin, self).get_form(request, obj, **kwargs)
        return form


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'description',
        'like',
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'message'
    ]