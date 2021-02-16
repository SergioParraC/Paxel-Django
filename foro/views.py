from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

#Formularios
from foro.forms import PostForm
#Modelos
from foro.models import foros_descrp
from django.contrib.auth.models import User

class DetailPostView(DetailView):
    model = foros_descrp
    template_name = 'foro/detailPost.html'

class CreatePostView(LoginRequiredMixin,CreateView):
    model = foros_descrp
    template_name = "foro/createPost.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["perfil"] = self.request.user.perfil
        return context
    
    
class ListPostsView(ListView):
    model = foros_descrp
    template_name = 'foro/listPost.html'

class UpdatePostView(LoginRequiredMixin,UpdateView):
    model = foros_descrp
    form_class = PostForm
    template_name = "foro/updatePost.html"

class DeletePostView(LoginRequiredMixin,DeleteView):
    model = foros_descrp
    template_name = "foro/deletePost.html"
    def get_success_url(self):
        return reverse('foro:index')
