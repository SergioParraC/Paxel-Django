from django.shortcuts import render

# Create your views here.
def inicio_view(request):
    return render(request,'foro/inicio.html')