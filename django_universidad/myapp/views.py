from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject, Student, Note
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