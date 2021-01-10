# Generated by Django 3.1.4 on 2021-01-09 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('nacim', models.DateField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='usuarios/images')),
                ('genero', models.CharField(max_length=15)),
                ('num_celular', models.BigIntegerField(blank=True, null=True)),
                ('pais', models.CharField(max_length=50)),
                ('biografia', models.TextField(blank=True, null=True)),
                ('sentecia', models.TimeField(blank=True, null=True)),
                ('llamados_atencion', models.IntegerField(blank=True, null=True)),
                ('nick', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BannData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contenido_comentario', models.CharField(blank=True, max_length=250, null=True)),
                ('foro_report', models.CharField(max_length=70)),
                ('codigo_foro', models.IntegerField()),
                ('causa', models.CharField(max_length=100)),
                ('id_comentario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foro.comentarios')),
                ('nick', models.ManyToManyField(to='usuarios.Perfil')),
            ],
        ),
    ]
