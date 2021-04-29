from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject, Student, Note, Teacher
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.


def subject(request):
    subjects = Subject.objects.all()
    response = ''
    for subject in subjects:
        print(subject.name)
        response = response + ' ' + subject.name

    print('estoy llamando al index')
    return HttpResponse(response)


def students(request):
    students = Student.objects.all()
    response = {}
    for student in students:
        print(student.first_name, student.last_name)
        response[student.id] = {
            'full name': '{} {}'.format(student.first_name, student.last_name),
        }
        enrollments = student.enrollment_set.all()
        logger.debug(enrollments)
        print(enrollments)
        student_enrollment = []

        for enrollment in enrollments:

            average_enrollment = 0
            notes = enrollment.note_set.all()
            logger.debug(notes)
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

    return JsonResponse(response)

def index(request):
    print('hola')
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request, 'home.html', context)

def list_students(request):
    print('hola')
    students = Student.objects.all()
    context = {
        'title':'Students',
        'students':students
    }
    return render(request, 'students.html', context)

def list_teachers(request):
    print('hola')
    teachers = Teacher.objects.all()
    context = {
        'title':'Teachers',
        'teachers':teachers
    }
    return render(request, 'teachers.html', context)

def list_persons(request,person):
    persons = Student
    if person == 'teacher':
        persons = Teacher
    persons = persons.objects.all()
    context = {
        'title':person,
        'persons':persons
    }
    return render(request,'list_persons.html',context)

def get_person(request, person, id):
    models = Student
    if person == 'teacher':
        models = Teacher
    persons = models.objects
    persons = persons.filter(id=id).first()
    context = {
        'title':person,
        'person':persons
    }
    return render(request,'get_person.html',context)


def new_student(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        Student(first_name=nombre,last_name=apellidos).save()
        return redirect('students')
    return render(request, 'new_student.html')



