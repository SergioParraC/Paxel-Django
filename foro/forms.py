from django import forms
#modelos
from django.contrib.auth.models import User
from foro.models import foros_descrp
from foro.models import videojuegos

class PostForm(forms.ModelForm):
    #crea un foro
    titulo = forms.CharField(
        min_length=5, 
        max_length=70,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Pon un titulo',
                'class':'form-control',
                'required':True,
                'autocomplete':"off"
                }
            )
        )
    contenido = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'Pon el contenido',
                'class':'form-control',
                'required':True
                }
            )
        )
    videojuego = forms.ModelChoiceField(
        queryset=videojuegos.objects.all(),
        empty_label="Selecciona un videojuego",
        widget=forms.Select(
            attrs={
                'class':'form-select',
                'required':True,
                }
            )
        )
    imagen = forms.FileInput()


    class Meta:
        model = foros_descrp
        fields= ['titulo','imagen','videojuego','contenido','creador']
        exclude = ['creador']
        