from django.contrib import admin
from .models import usuario
from .models import pelicula
# Register your models here.
admin.site.register(usuario)
admin.site.register(pelicula)