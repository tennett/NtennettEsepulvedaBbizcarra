from django.shortcuts import render
from .models import pelicula, user
from . import forms
def index (request):
# Create your views here.

    num_users = user.objects.all().count()
    return render(request, 'index.html', context={'num_books':num_users})

def view_crear_usuario(request):
    form= forms.CrearUsuario(request.POST or None)

    context={
        'formaReg': form
    }
    return render(request, 'registro', context)
