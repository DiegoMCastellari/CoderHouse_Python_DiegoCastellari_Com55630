from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuariosForm(UserCreationForm):

    email = forms.EmailField(label='Email de Usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Email de Usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=200)
    last_name = forms.CharField(label="Apellido/s", max_length=200)
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)