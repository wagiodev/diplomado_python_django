from django.contrib import admin
from django.urls import path
from .views import index,doctor


urlpatterns = [
    path('index', index),
    path('doctores',doctor)
]
