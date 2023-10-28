
from django.contrib import admin
from django.urls import path
from user_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # domain/get-info-user
    path("get-info-user", views.get_info_user),
    path("sign-in", views.sign_in)
]
