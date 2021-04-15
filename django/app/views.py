from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor
# Create your views here.

def index(request):
    print('Estoy llamando al index')
    return HttpResponse('Hola mundo')

def doctor(request):
    doctores = Doctor.objects.all()
    respuesta = ''
    for doctor in doctores:
        respuesta += ' '+doctor.nombre
        print('WALTER')
    return HttpResponse(respuesta)