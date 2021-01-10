from django.contrib.auth.models import User
from django.db import models

#Todos los datos de los usuarios
class Perfil(models.Model):
    nick = models.OneToOneField(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    nacim = models.DateField()
    imagen  = models.ImageField(
        upload_to='usuarios/images',
        blank=True,
        null=True
    )
    genero = models.CharField(max_length=15)
    num_celular = models.BigIntegerField(blank=True)
    pais = models.CharField(max_length = 50)
    biografia = models.TextField(blank=True)
    sentecia = models.TimeField(blank=True,null=True)
    llamados_atencion = models.IntegerField(blank=True,null=True)

#Tabla con los datos de sentencias con usuarios
class BannData(models.Model):
    nick = models.ManyToManyField("usuarios.Perfil")
    id = models.AutoField(primary_key=True)
    contenido_comentario = models.CharField(max_length=250, null=True, blank=True)
    foro_report = models.CharField(max_length=70)
    codigo_foro = models.IntegerField()
    id_comentario = models.OneToOneField("foro.comentarios", on_delete=models.CASCADE)
    causa = models.CharField(max_length=100)
    
