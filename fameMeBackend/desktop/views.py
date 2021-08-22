from django.shortcuts import render
from .models import Event, User


def index(request):
    query = Event.objects.all()
    data = {"events": query}
    return render(request, "index.html", context=data)


def bloggers(request):
    data = User.objects.filter(is_blogger=True)
    return render(request, "second_page.html", context={"bloggers": data})
