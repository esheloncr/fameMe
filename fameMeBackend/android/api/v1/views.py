from django.http import JsonResponse
from android.models import Event, User, Comment
from .serializers import ProfileSerializer, EventSerializer, EventCreateSerializer
from .services import add_like
from django.shortcuts import redirect, render
from rest_framework import mixins, viewsets, generics
from rest_framework.generics import get_object_or_404
from django.http import Http404
from rest_framework.decorators import action


def dev(request):
    query = Event.objects.all()
    data = {"events": query.first()}
    comm = Comment(message="testnew")
    comm.save()
    add_like(query.first(), User.objects.get(user=request.user))
    query.first().comments.add(comm)
    return render(request, "dev.html", context=data)


class BloggersViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = User.objects.filter(is_blogger=True)


class PeopleViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = User.objects.filter(is_blogger=False)


class EventRegister(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer


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


def vk_login(request):
    return redirect("/auth/login/vk-oauth2")


def inst_login(request):
    return redirect("/auth/login/instagram")
