from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Django
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
 
class Role(models.Model):
    """
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    """
    SUPER_ADMIN = 1
    REPAIRMENT = 2
    CLIENT = 3

    ALL_ROLES = [SUPER_ADMIN, REPAIRMENT, CLIENT]

    ROLE_CHOICES = (
        (SUPER_ADMIN, 'super_admin'),
        (REPAIRMENT, 'repairment'),
        (CLIENT, 'client'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.get_id_display()

    class Meta:
        db_table = 'role'

 


class User(AbstractUser):
    username = None
    email = None
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, unique=True)

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )
    must_change_password = models.BooleanField(default=False)

    # Roles and permissions
    roles = models.ManyToManyField(Role)

    USERNAME_FIELD = 'phone_number'

    # Locations
    country = models.CharField(max_length=255,  null=True)
    city = models.CharField(max_length=255,  null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.email})

    def get_roles(self):
        if self.roles.all():
            return self.roles.all()[0].name
        return ' -- '

    class Meta:
        db_table = 'user'




# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    cellphone = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='client')
    def __str__(self):
        return '{} {}'.format(self.name, self.address, self.cellphone)

class Repairman(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    cellphone = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='repairment')
    def __str__(self):
        return '{} {}'.format(self.name, self.address, self.cellphone)

class Appliance(models.Model):
    serial = models.CharField(max_length=30)
    trade_mark = models.CharField(max_length=30)
    id_client =  models.ForeignKey('Client', on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {}'.format(self.serial, self.trade_mark)
        
class Service(models.Model):
    description = models.TextField()
    date = models.DateField()
    id_client =  models.ForeignKey('Client', on_delete=models.CASCADE)
    id_repairman =  models.ForeignKey('Repairman', on_delete=models.CASCADE)
    id_appliance =  models.ForeignKey('Appliance', on_delete=models.CASCADE)
  


