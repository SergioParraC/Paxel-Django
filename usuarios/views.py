from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

#Modelos
from django.contrib.auth.models import User
from usuarios.models import Perfil

#Formularios
from usuarios.forms import Crear_Usuario_Form
from usuarios.forms import Act_Usuario_Form

def login_view(request):
    #Sistema de login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('usuarios:act_datos')
        else:
            return render(request, 'usuarios/login.html',{'error':'Usuario o contraseña erroneos'})
    return render(request,'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('usuarios:logout')

def crear_usuario(request):
    if request.method == 'POST':
        form = Crear_Usuario_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:login')
    else:
        form = Crear_Usuario_Form()
    return render(
        request=request,
        template_name='usuarios/crear_usuarios.html',
        context={
            'form':form,
            }
    )

@login_required
def act_datos_view(request):
    #Actualizar datos del usuario
    if request.method == 'POST':
        form = Act_Usuario_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foro:inicio')
    else:
        form = Act_Usuario_Form()
    return render(
        request=request,
        template_name='usuarios/actualizar_datos.html',
        context={
            'form':form,
            'user':request.user,
            'perfil':Perfil
        }
    )