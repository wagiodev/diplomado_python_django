from django.contrib import admin
from django.urls import path
from .views import client, repairman, register, login

urlpatterns = [
    path('client',      client,     name='client'),
    path('repairman',   repairman,  name='repairman'),
    path('register',    register,   name='register'),
    path('login',       login,      name='login')
]