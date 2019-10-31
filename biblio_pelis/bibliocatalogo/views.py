from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import pelicula, user
from django.views import generic
from . import forms
def index (request):
# Create your views here.
    num_users = user.objects.all().count()
    return render(request, 'index.html', context={'num_books':num_users})
#def view_crear_usuario(request):
#    form= forms.CrearUsuario(request.POST or None)
#
#   context={
#        'formaReg': form
#    }
#    return render(request, 'registro', context)

class creacion_usuario(CreateView):
    template_name='bibliocatalogo/usuario_registro.html'
    model=user
    fields='__all__'

class Actualizacion_usuario(UpdateView):
    template_name='bibliocatalogo/usuario_modificar.html'
    model=user
    fields=['nombre','email','password']  

class Eliminacion_usuario(DeleteView):
    model=user
    succes_url = reverse_lazy('user')

class DetalleVistaUsuario(generic.DetailView):
    template_name='bibliocatalogo/usuario_detail.html'
    model = user

class ListaUsuario(generic.ListView):
    template_name='bibliocatalogo/usuario_lista.html'
    model = user
    paginate_by = 15

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context"""