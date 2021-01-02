from django.contrib.auth.models import User
from django.db import models

class foros_list(models.Model):
    nick = models.OneToOneField(User, on_delete=models.CASCADE)
    ceacion = models.DateTimeField(auto_now=True, auto_now_add=True)
    titulo = models.CharField(max_length=70)
    #No se que base de datos utilizar para esto ni el tipo de relacion
    videojuego = models.OneToOneField(videojuego, max_length=100)
    descripcion = models.TextField()
    consola = models.CharField(max_length=20)
    codigo_foro = models.IntegerField()
    solicitud_moderacion = models.SmallIntegerField()
