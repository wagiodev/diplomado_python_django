from django.db import models

# Create your models here.


class Group(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(default='')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    group = models.ManyToManyField(Group)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Subject(models.Model):
    name = models.CharField(max_length=30)


class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)


class Note(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2)
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)





# class Estudiante(Person):
#     promedio = models.DecimalField(max_digits=5, decimal_places=2)

# class Profesor(Person):
#     pass

# class Materias(models.Model):
#     name = models.CharField(max_length=30)