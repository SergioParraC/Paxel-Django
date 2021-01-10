from django.contrib.auth.models import User
from django.db import models

class foros_descrp(models.Model):
    nick = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=70)
    #No se que base de datos utilizar para esto ni el tipo de relacion
    videojuego = models.ForeignKey('videojuegos', on_delete=models.CASCADE)
    resumen = models.TextField(max_length = 500)
    contenido = models.TextField()
    consola = models.CharField(max_length = 20)
    id_foro = models.AutoField(unique = True,primary_key=True)
    solicitud_moderacion = models.SmallIntegerField(null = True, blank = True)
    imagen = models.ImageField(upload_to='foros/images', null = True, blank = True)

class videojuegos(models.Model):
    nombre = models.ManyToManyField("usuarios.Perfil")
    genero = models.CharField(max_length=50)
    consola = models.CharField(max_length=50)
    estudio = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    version = models.CharField(max_length=5, null=True, blank=True)
    id_videojuego = models.AutoField(primary_key=True)

class comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    nick = models.ManyToManyField("usuarios.Perfil")
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    contenido = models.CharField(max_length=250)
    id_foro = models.ManyToManyField("foros_descrp")
    is_edit = models.BooleanField(null=True, blank=True)
    reportaro = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
