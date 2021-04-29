from django.contrib import admin
from django.urls import path
from .views import index, subject, students,list_students,list_teachers,list_persons,get_person,new_student

urlpatterns = [
    path('', index,name='home'),
    path('subject', subject),
    path('students', students),
    path('list_students', list_students,name='students'),
    path('list_teachers', list_teachers,name='teachers'),
    path('example/<person>',list_persons),
    path('example/<person>/<id>',get_person),
    path('student/new_student',new_student,name='new_student')
]