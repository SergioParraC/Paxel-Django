from django.contrib.auth.models import User
from django.db import models

class foros_descrp(models.Model):
    nick = models.OneToOneField(User, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=70)
    #No se que base de datos utilizar para esto ni el tipo de relacion
    videojuego = models.ForeignKey('videojuegos', on_delete=models.CASCADE)
    resumen = models.TextField(max_length = 500)
    contenido = models.TextField()
    consola = models.CharField(max_length = 20)
    codigo_foro = models.AutoField(unique = True,primary_key=True)
    solicitud_moderacion = models.SmallIntegerField(null = True, blank = True)
    imagen = models.ImageField(upload_to='foros/images', null = True, blank = True)

class videojuegos(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    consola = models.CharField(max_length=50)
    estudio = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField(auto_now=False, auto_now_add=False)