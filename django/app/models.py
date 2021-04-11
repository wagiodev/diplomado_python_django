from django.db import models

# Create your models here.
class Doctor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=30)

class Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=30)