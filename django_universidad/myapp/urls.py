from django.contrib import admin
from django.urls import path
from .views import subject, students

urlpatterns = [
    path('subject', subject),
    path('students', students)
]