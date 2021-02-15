from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse_lazy

#Formularios
from foro.forms import crearPostForm
#Modelos
from foro.models import foros_descrp

class DetailPostView(DetailView):
    model = foros_descrp
    template_name = 'foro/detailPost.html'

class CreatePostView(LoginRequiredMixin,CreateView):
    model = foros_descrp
    template_name = "foro/createPost.html"
    form_class = crearPostForm
    
class ListPostsView(ListView):
    model = foros_descrp
    template_name = 'foro/listPost.html'