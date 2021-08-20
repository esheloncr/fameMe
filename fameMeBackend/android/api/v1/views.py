from django.http import JsonResponse
from django.shortcuts import redirect


def dev(request):
    return JsonResponse({"message": "Hello"})


def vk_login(request):
    return redirect("/auth/login/vk-oauth2")


def inst_login(request):
    return redirect("/auth/login/instagram")
