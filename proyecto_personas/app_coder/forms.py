from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Alumnos_formulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    edad=forms.IntegerField()
    dni=forms.IntegerField()
    nacimiento=forms.DateField()

class Curso_formulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    camada=forms.IntegerField()
    turno=forms.CharField(max_length=15)


class EditarFormUsuario(UserCreationForm):

    email=forms.EmailField(label="Modificar")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=['email','password1','password1']
        help_text= {k:"" for k in fields}