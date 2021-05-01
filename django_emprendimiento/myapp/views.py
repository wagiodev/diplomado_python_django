from django.shortcuts import render, redirect
from .models import Client, Repairman, User, Role, Appliance, Service
from .forms import RegisterForm, LoginForm, ApplianceForm, ServiceForm
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
    msj= 'Accede a los servicios de Tecnimastercol.'
    if request.method == 'POST':
        form = RegisterForm(request.POST,rol_choices=ROL_CHOICES)
        if form.is_valid():
            
            name= request.POST.get('name')
            cellphone= request.POST.get('cellphone')
            address= request.POST.get('address')
            password = request.POST.get('password')
            rol = request.POST.get('rol')
            user = User.objects.create(
                phone_number=cellphone
            )
        
            user.set_password(password)
            user.save()
            role_object = Role.objects.get(id=rol)
            user.roles.add(role_object)
            logger.debug(rol)
            if rol == '1':
                Client(name=name,cellphone=cellphone,address=address,user=user).save()
            else:
                Repairman(name=name,cellphone=cellphone,address=address,user=user).save()
            return redirect('login')
        else:
            msj = 'Este número de celular ya existe en nuestro sistema'
    context = {
        'msj': msj,
        'form': form
    }    
    return render(request,'sesion/register.html', context)

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
                return redirect('cms')
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
    return render(request,'sesion/login.html', {'form': form})



    return render(request,'repairman.html')

@login_required(login_url='/service/login')
def cms(request):
    user = request.user
    appliances = None
    person = None
    services= None
    appliances = None
    if has_role(user, 'Client'):
        person = Client.objects.filter(user_id=user).first()
        services = Service.objects.filter(id_client=person)
        appliances = Appliance.objects.filter(id_client=person)
    elif has_role(user,'Repairman'):
        return redirect('cms_repairman')
    context = {
        'person': person,
        'services':services,
        'appliances':appliances
    }
    return render(request,'cms/cms.html',context)

@login_required(login_url='/service/login')
def cms_repairman(request):
    user = request.user
    appliances = None
    person = None
    services= None
    person = Repairman.objects.filter(user_id=user).first()
    services = Service.objects.filter(id_repairman=person)
    context = {
        'person': person,
        'services':services,
    }
    return render(request,'cms/cms_repairman.html',context)

@login_required(login_url='/service/login')
def newAppliance(request):
    form = ApplianceForm()
    person = None
    user = request.user
    msj = ''
    if request.method == 'POST':
        form = ApplianceForm(request.POST)
        if form.is_valid():
            serial= request.POST.get('serial')
            trade_mark = request.POST.get('trade_mark')
            client = Client.objects.filter(user_id=user).first()
            Appliance(serial=serial, trade_mark=trade_mark, id_client=client).save()
            return redirect('cms')
        else:
            msj='Prueba con otro aparato que no este registrado'
    user = request.user
    if has_role(user, 'Client'):
        person = Client.objects.filter(user_id=user).first()
    elif has_role(user,'Repairman'):
        person = Repairman.objects.filter(user_id=user).first()
    context = {
        'msj':msj,
        'person': person,
        'form': form
    }
    return render(request,'cms/new_appliance.html',context)

@login_required(login_url='/service/login')
def newService(request):
    user = request.user
    client = Client.objects.filter(user_id=user).first()
    group_appliances = Appliance.objects.filter(id_client = client).values_list('id', 'trade_mark')
    group_repairman = Repairman.objects.all().values_list('id', 'name')
    form = ServiceForm(appliance_choices=group_appliances, repairman_choices=group_repairman)
    person = None
 
    if request.method == 'POST':
        form = ServiceForm(request.POST,appliance_choices=group_appliances, repairman_choices=group_repairman)
        if form.is_valid():
            description= request.POST.get('description')
            date = request.POST.get('date')
            id_appliance = request.POST.get('appliance')
            id_repairman = request.POST.get('repairman')
            appliance = Appliance.objects.filter(id=id_appliance).first()
            repairman = Repairman.objects.filter(id=id_repairman).first()
            client = Client.objects.filter(user_id=user).first()
            Service(description=description, date=date, id_appliance=appliance, id_client=client, id_repairman=repairman).save()
            return redirect('cms')
        
    if has_role(user, 'Client'):
        person = Client.objects.filter(user_id=user).first()
    elif has_role(user,'Repairman'):
        person = Repairman.objects.filter(user_id=user).first()
    context = {
        'person': person,
        'form': form
    }
    return render(request,'cms/new_service.html',context)

def logout(request):
    auth_logout(request)
    return redirect('login')

def has_role(user, names):
    role_names = names.split(',')
    if hasattr(user, 'roles'):
        if user.roles.filter(name__in=role_names).exists():
            return True
    return False

    



