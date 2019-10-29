from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ,name='index')
    
]

urlpatterns += [
    path('registro/', views.creacion_usuario.as_view(), name='CreateView'),
    path('<pk>/borrar/', views.Actualizacion_usuario.as_view(), name="DeleteView"),
    path("listaUsuarios/", views.ListaUsuario.as_view(), name="listaUsuarios")
]