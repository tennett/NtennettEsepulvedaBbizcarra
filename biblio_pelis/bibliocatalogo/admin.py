from django.contrib import admin
from .models import user
from .models import pelicula
# Register your models here.
admin.site.register(user)
admin.site.register(pelicula)