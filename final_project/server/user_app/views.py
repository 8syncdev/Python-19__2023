from django.shortcuts import render
from django.http import JsonResponse
from .models import User

# Create your views here.


def get_info_user(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username, password=password)
        user.save()
        return JsonResponse({
            "username": user.username,
            "password": user.password
        })
    
    return JsonResponse({
            "err":"Lỗi rồi"
        })

def sign_in(request):
    try:
        if request.method == "POST":
            user = User.objects.get(username=request.POST.get('username'))
            return JsonResponse({
                "detail":"success",
                "username": user.username,
                "password": user.password
            })
    except Exception as e:
        return JsonResponse({
            "detail": "error"
        })