from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('list_students',   views.list_students,    name='list_students'),
    path('list_teachers',   views.list_teachers,    name='list_teachers'),

    path('students',        views.students,         name='students'),
    path('student/new',     views.new_student,      name='new_student'),
    path('student/<id>',    views.get_student,      name='get_student'),

    path('groups',          views.groups,           name='groups'),
    path('group/new',       views.new_group,        name='new_group'),
    path('group/<id>',      views.get_group,        name='get_group'),

    path('teachers',        views.teachers,         name='teachers'),
    path('teacher/new',     views.new_teacher,      name='new_teacher'),
    path('teacher/<id>',    views.get_teacher,      name='get_teacher'),


    path('example/<person>/', views.list_person),
    path('example/<person>/<id>', views.get_person),
]
