from django.db import models
from django.urls import reverse
import uuid

class usuario(models.Model):

    id = models.AutoField(primary_key=True, editable = False)
    nombre = models.CharField(max_length=50, help_text="Nombre", blank=False)
    email = models.EmailField(max_length=50, help_text="Email usuario", blank=False)
    password = models.CharField(max_length=30, help_text="Contraseña usuario", blank=False)

    def __str__(self):

        return str(self.id)
    
    def get_absolute_url(self):
        return reverse("usuario_detail", args=[str(self.id)])

class pelicula(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_pelicula = models.CharField(max_length=60,help_text="Nombre de pelicula")
    genero = models.CharField(max_length=100, help_text="Genero de la")
    año = models.DateField(null=True)

    def __str__(self):
        return f'{self.id}, {self.nombre_pelicula}'
    
    
    def get_absolute_url(self):
        return reverse("pelicula_detail", args=[str(self.id)])