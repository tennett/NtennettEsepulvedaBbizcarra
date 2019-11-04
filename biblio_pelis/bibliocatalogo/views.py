from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import pelicula, usuario
from django.views import generic
from . import forms

def index (request):
    num_users = usuario.objects.all().count()
    return render(request, 'index.html')

def view_crear_usuario(request):
    form= forms.CrearUsuario(request.POST or None)
    
    context={
            'formaReg': form
       }
    return render(request, 'usuario_registro', context)

def register(request):
    registered = False
    if request.method == 'POST':
        usuario_form = usuarioForm(data=request.POST)
        if usuario_form.is_valid():
            user = usuario_form.save()
            user.set_password(usuario.password)
            user.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        usuario_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

class creacion_usuario(CreateView):
    template_name='bibliocatalogo/usuario_registro.html'
    model=usuario
    fields='__all__'

class Actualizacion_usuario(UpdateView):
    template_name='bibliocatalogo/usuario_modificar.html'
    model=usuario
    fields=['nombre','email','password']  

class Eliminacion_usuario(DeleteView):
    model=usuario
    succes_url = reverse_lazy('user')

class DetalleVistaUsuario(generic.DetailView):
    template_name='bibliocatalogo/usuario_detail.html'
    model = usuario

class ListaUsuario(generic.ListView):
    template_name='bibliocatalogo/usuario_lista.html'
    model = usuario
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context