from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class user(models.Model):
    """
    Una clase típica definiendo un modelo, derivado desde la clase Model.
    """
    # Campos
    nombre = models.CharField(max_length=50, help_text="Nombre", blank=False)
    email = models.EmailField(max_length=50, primary_key=True, help_text="Email usuario", blank=False)
    password = models.CharField(max_length=30, help_text="Contraseña usuario", blank=False)
    # Métodos
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en elsitio de Admin, etc.)
        """
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("user_detail", args=[str(self.pk)])
    
class pelicula(models.Model):
    nom = models.CharField(max_length=60, blank=False)