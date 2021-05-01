from django.contrib import admin
from django.urls import path
from .views import register, login, cms, newAppliance, newService, cms_repairman, logout

urlpatterns = [
    path('register',    register,   name='register'),
    path('login',       login,      name='login'),
    path('cms',         cms,        name='cms'),
    path('cms_repairman',         cms_repairman,        name='cms_repairman'),
    path('new_appliance',newAppliance, name='new_appliance'),
    path('new_service',newService, name='new_service'),
    path('logout',   logout,    name='logout'),
]