from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir la Contraseña', widget= forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name' ]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar E-mail")
    first_name = forms.CharField(label = 'Nombre')
    password1 = forms.CharField(label = 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir la Contraseña', widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
            