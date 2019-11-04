from django import forms
from django.contrib.auth.models import User
from .models import  usuario, pelicula
from tkinter.test.support import widget_eq

"""
class FormaUsuario (forms.ModelForm):
    nombre = forms.CharField(max_length=50, help_text="Nombre", blank=False)
    email = forms.EmailField(max_length=50, help_text="Email usuario", blank=False)
    passw = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = usuario
        fields = ('nombre', 'email', 'passw')"""
        