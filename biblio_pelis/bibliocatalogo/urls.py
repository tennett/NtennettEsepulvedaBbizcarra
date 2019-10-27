from django.urls import path
from .views import index, view_crear_usuario


urlpatterns = [
    path('',views.index,name='index'),
    path('', views.view_crear_usuario, name='registro')
]
