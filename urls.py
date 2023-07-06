"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name='index'),
    path("user",views.usert,name='user'),
    path("food",views.foddie,name='food'),
    path("uploaduser",views.uploaduser,name='uploaduser'),
    path("uploadfood",views.uploadfood,name='uploadfood'),
    path("uploadreview",views.uploadreview,name='uploadreview'),
    path("editreview/<int:uid>",views.editreview,name='editreview'),
    path("deleteR/<int:rid>",views.deleteR,name='deleteR'),
    path("edituser/<str:uname>",views.edituser,name='edituser'),
    path("deleteU/<str:uname>",views.deleteU,name='deleteU'),
    path("editfood/<str:fname>",views.editfood,name='editfood'),
    path("deletefood/<str:fname>",views.deleteF,name='deletefood'),
    path("register",views.CreateUser,name='register'),
    path("login",views.sign_in,name='login'),
    path('logout',views.sign_out,name="logout"),
]
