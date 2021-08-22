from django.shortcuts import render
from .models import Event, User


def index(request):
    query = Event.objects.all()
    data = {"events": query}
    return render(request, "index.html", context=data)


def bloggers(request):
    data = User.objects.filter(is_blogger=True)
    for i in data:
        try:
            print(i.profile_photo.image.url)
        except:
            pass
    return render(request, "second_page.html", context={"bloggers": data})


def video_chat(request):
    return render(request, "third_page.html")
