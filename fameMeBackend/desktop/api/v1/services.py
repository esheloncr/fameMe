from desktop.models import User


def add_like(obj, user_id):
    user = User.objects.get(pk=user_id)
    if user in obj.liked_by.all():
        obj.like -= 1
        if obj.like < 0:
            obj.like = 0
        obj.liked_by.remove(user)
    else:
        obj.like += 1
        obj.liked_by.add(user)
    obj.save()

