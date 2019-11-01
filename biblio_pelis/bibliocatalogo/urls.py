from django.urls import path
from django.views.generic import ListView
from . import views


urlpatterns = [
   path('', views.index ,name='index')
]

urlpatterns += [
    path('usuarioregistro/', views.creacion_usuario.as_view(), name='CreateView'),
    #path('borrar/', , name="DeleteView"),
    path('listausuarios/', views.ListaUsuario.as_view(), name='ListView'),
    path('usuariodetail/<int:id>',views.DetalleVistaUsuario.as_view(),name='DetailView')
]