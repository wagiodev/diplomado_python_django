from django import forms
from django.forms import ValidationError

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

class LoginForm(forms.Form):
    def __init__(self, *args, rol_choices=(), **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['rol'].choices = rol_choices

    cellphone = forms.CharField(max_length=30, required=True, label="celular",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ))
    
    name = forms.CharField(max_length=30, required=True, label="Nombre",
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

class ServiceForm(forms.Form):
    def __init__(self, *args, appliance_choices=(),repairman_choices=(), **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['appliance'].choices = appliance_choices
        self.fields['repairman'].choices = repairman_choices

    description = forms.CharField(required=True, label="descripcion",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ))

    date = forms.DateField(required=True, label="descripcion",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ))

    appliance = forms.ChoiceField(
        required=True,
        label="Selecciona tu rol",
        widget=forms.Select(attrs={
            # 'style': "width: 100%",
            'class': 'form-control',
        }))
    
    repairman = forms.ChoiceField(
        required=True,
        label="Selecciona tu rol",
        widget=forms.Select(attrs={
            # 'style': "width: 100%",
            'class': 'form-control',
        }))
        