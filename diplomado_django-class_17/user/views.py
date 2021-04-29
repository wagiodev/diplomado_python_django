from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('saludo')

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('saludo')

def saludo(request):
    return render(request, 'saludo.html')

@login_required(login_url='/user/login/')
def info(request):
    return render(request, 'info.html')
