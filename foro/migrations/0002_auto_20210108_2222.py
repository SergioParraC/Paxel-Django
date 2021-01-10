# Generated by Django 3.1.4 on 2021-01-09 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videojuegos',
            name='nombre',
            field=models.ManyToManyField(to='usuarios.Perfil'),
        ),
        migrations.AddField(
            model_name='foros_descrp',
            name='nick',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='foros_descrp',
            name='videojuego',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foro.videojuegos'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='id_foro',
            field=models.ManyToManyField(to='foro.foros_descrp'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='nick',
            field=models.ManyToManyField(to='usuarios.Perfil'),
        ),
    ]