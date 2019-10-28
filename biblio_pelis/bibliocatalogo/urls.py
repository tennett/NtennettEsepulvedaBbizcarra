from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ,name='index')
    
]

urlpatterns += [
    path('registro/', views.creacion_usuario.as_view(), name='user_form')
    
]