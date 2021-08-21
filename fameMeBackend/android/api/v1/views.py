from django.http import JsonResponse
from android.models import Event, User, Comment
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProfileSerializer, EventSerializer, EventCreateSerializer, UserSerializer
from .services import add_like
from django.shortcuts import redirect, render
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from django.http import Http404
from rest_framework.decorators import action
import json


def dev(request):
    events = Event.objects.all()
    users = User.objects.all()
    comments = Comment.objects.all()
    data = {
        "events": events,
        "users": users,
        "comments": comments,
    }
    for i in events:
        print(not i.liked_by.count())
    return render(request, "dev.html", context=data)


class BloggersViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = User.objects.filter(is_blogger=True)
    permission_classes = [AllowAny, ]


class PeopleViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = User.objects.filter(is_blogger=False)
    permission_classes = [AllowAny, ]


class EventRegister(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = [AllowAny, ]

    @action(detail=False, methods=['GET'])
    def get(self, request):
        return JsonResponse({"message": "send 'author' and 'description' fields"})


class EventApiView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny, ]


def get_user(request, pk):
    try:
        query = User.objects.get(pk=pk)
        data = UserSerializer(query).data
        return JsonResponse({"user": data})
    except:
        raise Http404


def get_event(request, pk):
    query = get_object_or_404(Event.objects.all(), pk=pk)
    serializer = EventSerializer(query)
    return JsonResponse({"message": serializer.data})


def like(request, pk):
    try:
        query = Event.objects.get(pk=pk)
    except:
        raise Http404
    add_like(query, request.user.pk)
    return JsonResponse({"message": query.like})


@csrf_exempt
def comment(request, pk):
    if request.method == "POST":
        event = Event.objects.get(pk=pk)
        comment = json.loads(request.body.decode()).get("comment")
        event.comments.update_or_create(message=comment)
        return JsonResponse({"message": f"{comment} successfully added"})
    raise Http404


def vk_login(request):
    return redirect("/auth/login/vk-oauth2")


def inst_login(request):
    return redirect("/auth/login/instagram")
