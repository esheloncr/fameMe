from django.http import JsonResponse


def dev(request):
    return JsonResponse({"message": "hello"})