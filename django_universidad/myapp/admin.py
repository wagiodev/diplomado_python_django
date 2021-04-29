from django.contrib import admin
from .models import Student, Teacher, Subject, Enrollment, Note

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Enrollment)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'student','teacher','subject')



# Register your models here.
