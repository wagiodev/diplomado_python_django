from django.shortcuts import render, redirect
from .models import Client, Repairman, User, Role
from .forms import RegisterForm, LoginForm
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
ROL_CHOICES =(
    ("1", "Cliente"),
    ("2", "Técnico")
)
def register(request):
    
    form = RegisterForm(rol_choices=ROL_CHOICES)
    if request.method == 'POST':
        form = RegisterForm(request.POST,rol_choices=ROL_CHOICES)
        if form.is_valid():
            name= form.cleaned_data['name']
            cellphone= form.cleaned_data['cellphone']
            address= form.cleaned_data['address']
            password = form.cleaned_data['password']
            rol = form.cleaned_data['rol']
            user = User.objects.create(
                phone_number=cellphone
            )
            user.set_password(password)
            user.save
            role_object = Role.objects.get(id=rol)
            user.roles.add(role_object)
            logger.debug(rol)
            if rol == '1':
                Client(name=name,cellphone=cellphone,address=address,user=user).save()
            else:
                Repairman(name=name,cellphone=cellphone,address=address,user=user).save()
            return redirect('login')
    return render(request,'register.html', {'form': form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cellphone= form.cleaned_data['cellphone']
            password= form.cleaned_data['password']
            appliances = None
            user = authenticate(phone_number=cellphone, password=password)
            if user:
                auth_login(request, user)
                return redirect('client')
        # if rol == '1':
        #     person = Client.objects.filter(cellphone=cellphone).first()
        #     appliances = person.appliance_set.all()
        #     redic = 'client.html'
        # else:
        #     person = Repairman.objects.filter(cellphone=cellphone).first()
        #     redic = 'repairman.html'
        # services = person.service_set.all()
        
        # context = {
        #     'person': person,
        #     'appliances':appliances,
        #     'services':services
        # }
        """ user = request.user
        
        cliente = Client.objects.filter(user=user)
        Service(,,id_client=cliente) """
        return render(request, redic, context)
    return render(request,'login.html', {'form': form})


def client(request):
    
    return render(request,'client.html')

def repairman(request):
    return render(request,'repairman.html')



