from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Subject, Student, Teacher, Group
from .forms import GroupForm, StudenFrom, TeacherFrom
# Create your views here.


def home(request):
    context = {}
    return render(request, 'home.html', context)


def list_students(request):
    response = get_students()
    return JsonResponse(response)


def list_teachers(request):
    teachers = Teacher.objects.all().values_list('id', 'first_name')
    context = {
        'title': 'Profesores',
        'teachers': list(teachers)
    }

    return JsonResponse(context)


def get_students():
    students = Student.objects.all()
    response = {}
    for student in students:
        print(student.first_name, student.last_name)
        response[student.id] = {
            'full name': '{} {}'.format(student.first_name, student.last_name),
        }
        enrollments = student.enrollment_set.all()
        student_enrollment = []

        for enrollment in enrollments:

            average_enrollment = 0
            notes = enrollment.note_set.all()
            if notes:
                for note in notes:
                    average_enrollment = average_enrollment + note.value

                average_enrollment = average_enrollment / len(notes)
            student_enrollment.append(
                {
                    'name': enrollment.subject.name,
                    'average': average_enrollment
                }
            )

        response[student.id]['enrollments'] = student_enrollment
    return response


def students(request):
    students = Student.objects.all()
    context = {
        'title': 'Estudiantes',
        'students': students
    }

    return render(request, 'student/list_students.html', context)

def get_student(request, id):
    student = Student.objects.filter(id=id).first()
    groups = student.group.all()
    context = {
        'title': 'student',
        'groups': groups,
        'student': student
    }

    return render(request, 'student/detail_student.html', context)

def new_student(request):
    group_choices = Group.objects.all().values_list('id', 'title')
    form = StudenFrom(group_choices=group_choices)
    if request.method == 'POST':
        form = StudenFrom(request.POST, group_choices=group_choices)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            group_choices = form.cleaned_data['group']

            student = Student(first_name=first_name, last_name=last_name)
            student.save()

            student.group.add(group_choices)

            return redirect('students')

    return render(request, 'student/new_student.html', {'form': form})



def groups(request):
    groups = Group.objects.all()
    context = {
        'title': 'Groups',
        'groups': groups
    }

    return render(request, 'group/list_groups.html', context)

def get_group(request, id):

    group = Group.objects.filter(id=id).first()
    students = group.student_set.all()
    context = {
        'title': group.title,
        'group': group,
        'students': students
    }

    return render(request, 'group/detail_group.html', context)

def new_group(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)

        if form.is_valid():
            description = form.cleaned_data['description']
            title = form.cleaned_data['title']

            Group(title=title, description=description).save()
            return redirect('groups')

    return render(request, 'group/new_group.html', {'form': form})


def teachers(request):
    teachers = Teacher.objects.all()
    context = {
        'title': 'Profesores',
        'teachers': teachers
    }

    return render(request, 'teacher/list_teachers.html', context)

def get_teacher(request, id):
    teacher = Teacher.objects.filter(id=id).first()
    context = {
        'title': 'teacher',
        'teacher': teacher
    }

    return render(request, 'teacher/detail_teacher.html', context)

def new_teacher(request):
    form = TeacherFrom()
    if request.method == 'POST':
        form = TeacherFrom(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            teacher = Teacher(first_name=first_name, last_name=last_name)
            teacher.save()


            return redirect('teachers')

    return render(request, 'teacher/new_teacher.html', {'form': form})


def list_person(request, person):
    models = Student
    if person == 'teacher':
        models = Teacher

    persons = models.objects.all()
    context = {
        'title': person,
        'persons': persons
    }
    return render(request, 'person/list_person.html', context)

def get_person(request, person, id):
    models = Student
    if person == 'teacher':
        models = Teacher

    persons = models.objects
    person = persons.filter(id=id).first()
    context = {
        'title': person,
        'person': person
    }
    return render(request, 'person/person_detail.html', context)
