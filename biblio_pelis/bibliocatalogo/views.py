from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import pelicula, user
from django.views import generic
from . import forms

def view_crear_usuario(request):
    form= forms.CrearUsuario(request.POST or None)

    context={
        'formaReg': form
    }
    return render(request, 'registro.html', context)

class creacion_usuario(CreateView):
    model=user
    fields='__all__'

class Actualizacion_usuario(UpdateView):
    model=user
    fields=['nombre','email','password']  

class Eliminacion_usuario(DeleteView):
    model=user
    succes_url = reverse_lazy('user')

class DetalleVistaUsuario(generic.DetailView):
    model=user

