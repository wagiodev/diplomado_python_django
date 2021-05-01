from django import forms
from django.forms import ValidationError
from .models import User, Appliance
from datetime import date

class RegisterForm(forms.Form):
    def __init__(self, *args, rol_choices=(), **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['rol'].choices = rol_choices

   
    name = forms.CharField(max_length=30, required=True, label="Nombre",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ))
    
    cellphone = forms.CharField(max_length=30, required=True, label="celular",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ))
    address = forms.CharField(max_length=30, required=True, label="adress",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ))
        
    rol = forms.ChoiceField(
        required=True,
        label="Selecciona tu rol",
        widget=forms.Select(attrs={
            # 'style': "width: 100%",
            'class': 'form-control',
        }))

    password=forms.CharField(widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
        }
    ))
    def clean(self):
        cellphone = self.cleaned_data['cellphone']
        if User.objects.filter(phone_number=cellphone).exists():
            raise forms.ValidationError('Looks like email already exists')
        return cellphone

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        

    cellphone = forms.CharField(max_length=30, required=True, label="celular",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ))
    
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
        }
    ))
    """ rol = forms.ChoiceField(
        required=True,
        label="Selecciona tu rol",
        widget=forms.Select(attrs={
            # 'style': "width: 100%",
            'class': 'form-control',
        })) """

class ServiceForm(forms.Form):
    def __init__(self, *args, appliance_choices=(), repairman_choices=(), **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['appliance'].choices = appliance_choices
        self.fields['repairman'].choices = repairman_choices

    description = forms.CharField(required=True, label="descripcion",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'data-target': '#datetimepicker1'
            }
        ))

    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'min':date.today()
        }))

    appliance = forms.ChoiceField(
        required=True,
        label="Selecciona tu aparato",
        widget=forms.Select(attrs={
            # 'style': "width: 100%",
            'class': 'form-control',
        }))
    
    repairman = forms.ChoiceField(
        required=True,
        label="Seleccionar técnico",
        widget=forms.Select(attrs={
            # 'style': "width: 100%",
            'class': 'form-control',
        }))

class ApplianceForm(forms.Form):
    serial = forms.CharField(required=True, label="Serial",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ps-0 form-control-line',
            }
        ))

    trade_mark = forms.CharField(required=True, label="Tipo y Marca",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ps-0 form-control-line',
            }
        ))
    def clean(self):
        serial= self.cleaned_data['serial']
        if Appliance.objects.filter(serial=serial).exists():
            raise forms.ValidationError('Looks like email already exists')
        return serial
    
    
                