from django.db import models

# Create your models here.
class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=30)

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=30)
class Citas(models.Model):
    id_doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente , on_delete=models.CASCADE)
    fecha = models.DateField()
class Notas(models.Model):
    id_cita = models.ForeignKey(Citas, on_delete=models.CASCADE)
    nota = models.TextField()
    