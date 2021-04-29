
from django.urls import path
from . import views

urlpatterns = [
    path('login/',    views.login,     name='login'),
    path('logout/',   views.logout,    name='logout'),
    path('saludo/',   views.saludo,    name='saludo'),
    path('info/',     views.info,      name='info'),
]
