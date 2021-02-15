from django.contrib.auth.models import User
from django.db import models

class videojuegos(models.Model):
    id_videojuego = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    consola = models.CharField(max_length=50)
    estudio = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    version = models.CharField(max_length=5, null=True, blank=True)
    def __str__(self):
        return str(self.nombre)

class foros_descrp(models.Model):
    id_foro = models.AutoField(primary_key=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    videojuego = models.ForeignKey(videojuegos,on_delete=models.DO_NOTHING)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=70)
    imagen = models.ImageField(upload_to='foros/images', null = True, blank = True)
    contenido = models.TextField()

    def get_absolute_url(self):
        return '/foro/%s' %(self.pk)
    class Meta:
        ordering = ['-fecha_creacion']
    
class comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    foro = models.ForeignKey("foro.foros_descrp", on_delete=models.CASCADE)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_editado = models.DateTimeField(auto_now=True)
    contenido = models.CharField(max_length=250)
    is_edit = models.BooleanField(default=False)
    
class likes(models.Model):
    id_like = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    foro = models.ForeignKey("foro.foros_descrp", on_delete=models.DO_NOTHING)
    comentario = models.ForeignKey("foro.comentarios", on_delete=models.DO_NOTHING)