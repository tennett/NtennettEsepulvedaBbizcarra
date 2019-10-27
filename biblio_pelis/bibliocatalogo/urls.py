from django.urls import path
from .views import index, view_crear_usuario


urlpatterns = [
    path('', index,name='index'),
    path('', view_crear_usuario, name='registro')
]
