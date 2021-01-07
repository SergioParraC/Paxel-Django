from django.contrib.auth.models import User
from django.db import models

#Todos los datos de los usuarios
class Perfil(models.Model):
    nick = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen  = models.ImageField(
        upload_to='usuarios/images',
        blank=True,
        null=True
    )
    creado = models.DateTimeField(auto_now_add=True)
    nacim = models.DateField()
    num_celular = models.BigIntegerField(blank=True,null=True)
    pais = models.CharField(max_length = 50)
    biografia = models.TextField(blank=True,null=True)
    sentecia = models.DurationField(blank=True,null=True)

#Tabla con los datos de sentencias con usuarios
class BannData(models.Model):
    nick = models.ManyToManyField(User)
    codigo_foro = models.IntegerField()
    titulo = models.CharField(max_length=70)
    causa = models.CharField(max_length=100)
    
