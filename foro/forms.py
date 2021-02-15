from django import forms
#modelos
from django.contrib.auth.models import User
from foro.models import foros_descrp
from foro.models import videojuegos

class crearPostForm(forms.ModelForm):
    #crea un foro
    titulo = forms.CharField(min_length=5 , max_length=70)
    resumen = forms.CharField(min_length=30, max_length=500)
    contenido = forms.CharField()
    videojuego = forms.ModelChoiceField(queryset=videojuegos.objects.all())
    
    class Meta:
        model = foros_descrp
        fields= ['titulo','resumen','contenido','videojuego']

    