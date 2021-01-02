from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Perfil(models.Model):
    nick = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen  = models.ImageField(
        upload_to='usuarios/imagen',
        blank=True,
        null=True
    )
    creado = models.DateTimeField(auto_now_add=True)
    nacim = models.DateField()
    num_celular = models.BigIntegerField(blank=True,null=True)
    pais = models.CharField(max_length = 50)
    biografia = models.TextField(blank=True,null=True)
    sentecia = models.DurationField(blank=True,null=True)
    