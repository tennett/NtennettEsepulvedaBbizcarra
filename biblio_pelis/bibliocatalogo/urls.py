from django.urls import path
from . import views


urlpatterns = [
    path('', index,name='index'),
    path('', view_crear_usuario, name='registro')
    path('user/<int:pk>',views.DetalleVistaUsuario.as_view(),name='user-detail')
]
urlpatterns += [
    path('user/create/',views.creacion_usuario.as_view(),name='user_create'),
    path('user/<int:pk>/update/',views.Actualizacion_usuario.as_view(),name='user_update'),
    path('user/<int:pk>/delete/',views.Eliminacion_usuario.as_view(),name='user_delete'),
    
]

