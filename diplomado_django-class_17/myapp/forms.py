from django import forms

class GroupForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)


class StudenFrom(forms.Form):
    def __init__(self, *args, group_choices=(), **kwargs):
        super(StudenFrom, self).__init__(*args, **kwargs)
        self.fields['group'].choices = group_choices

    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, required=True, label="Nombre",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Nombre",
                'class': 'form-control',
            }
        ))

    last_name = forms.CharField(max_length=30, required=True, label="Apellido",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Apellido",
                'class': 'form-control',
            }
        ))
    
    group = forms.ChoiceField(
        required=False,
        label="Grupo",
        widget=forms.Select(attrs={
            # 'style': "width: 100%",
            'class': 'form-control',
        }))

class TeacherFrom(forms.Form):

    first_name = forms.CharField(max_length=30, required=True, label="Nombre",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Nombre",
                'class': 'form-control',
            }
        ))

    last_name = forms.CharField(max_length=30, required=True, label="Apellido",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Apellido",
                'class': 'form-control',
            }
        ))
    
