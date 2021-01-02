from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    #Sistema de login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'usuarios/login.html',{'error':'Usuario o contraseña erroneos'})
    return render(request,'usuarios/login.html')