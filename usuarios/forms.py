from django import forms
from django.forms.widgets import TextInput
#Modelos
from django.contrib.auth.models import User
from usuarios.models import Perfil

class Crear_Usuario_Form(forms.Form):
    #Formulario para crear usuarios

    username = forms.CharField(
        min_length=6, 
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Usuario o Nick',
                'class':'form-control',
                'required':True}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Correo elecrónico',
                'class':'form-control',
                'required':True}
        )
    )
    password = forms.CharField(
        min_length=8, 
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña',
                'class':'form-control',
                'required':True}
        )
    )
    
    password_confirmation = forms.CharField(
        min_length=8, 
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Vuelva a escribir la contraseña',
                'class':'form-control',
                'required':True}
        )
    )
    first_name = forms.CharField(
        min_length=3, 
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nombre',
                'class':'form-control',
                'required':True}
        )
    )
    last_name = forms.CharField(
        min_length=3, 
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Apellido',
                'class':'form-control',
                'required':True}
        )
    )
    pais = forms.CharField(
        min_length=3, 
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Pais de origen',
                'class':'form-control',
                'required':True}
        )
    )
    nacim = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder':'DD/MM/AAAA',
                'class':'form-control',
                'required':True}
        )
    )
    
    def clean(self):
        #verifica si las contraseñas son igules
        data=super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return data
    
    def clean_username(self):
        #Revisa si exite una cuenta con el nick
        data=super().clean()
        username = data['username']
        username_en_uso = User.objects.filter(username=username).exists()
        if username_en_uso:
            raise forms.ValidationError('El nombre de usuario ya existe, pruebe con otro')
        return username
    
    def clean_email(self):
        #Revisa si exite una cuenta con este email
        data=super().clean()
        email = data['email']
        email_en_uso = User.objects.filter(email=email).exists()
        if email_en_uso:
            raise forms.ValidationError('Ya existe una cuenta con este email')
        return email

    def save(self):
        #Guardando datos
        data = self.cleaned_data
        #pasando y elminando datos no pertenecientes al modelo User
        data.pop('password_confirmation')
        pais = data['pais']
        data.pop('pais')
        nacim = data['nacim']
        data.pop('nacim')
        user=User.objects.create_user(**data)
        #Guardando en el modelo perfil
        perfil = Perfil(nick=user,pais=pais,nacim=nacim)
        perfil.save()

class Act_Usuario_Form(forms.Form):
    email = forms.EmailField(required=True)
    genero = forms.CharField(min_length=3, max_length=20, required=True)
    first_name = forms.CharField(min_length=3, max_length=15, required=True)
    last_name = forms.CharField(min_length=3, max_length=15, required=True)
    num_celular = forms.IntegerField(required=False)
    biografia = forms.CharField(max_length=500, required=False)

    def clean_email(self):
        #Revisa si exite una cuenta con este email
        data=super().clean()
        email = data['email']
        email_en_uso = User.objects.filter(email=email).exists()
        if email_en_uso:
            raise forms.ValidationError('Ya existe una cuenta con este email')
        return email

    def save(self):
        #Guardando datos
        data = self.cleaned_data
        #Asignanado datos por variable
        email = data['email']
        genero = data['genero']
        first_name = data['first_name']
        last_name = data['last_name']
        num_celular = data['num_celular']
        biografia = data['biografia']
        #Guardando en el modelo Users
        user = User(first_name=first_name, last_name=last_name)
        user.save()
        perfil = Perfil(email=email, genero=genero, num_celular=num_celular, biografia=biografia)

