from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#Formularios
from foro.forms import PostForm
#Modelos
from foro.models import foros_descrp
from django.contrib.auth.models import User

def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    context = self.get_context_data(object=self.object)
    if (str(self.request.user.username) == str(self.object.creador)):
        context['isCreador'] = True
    else:
        context['isCreador'] = False
    return self.render_to_response(context)

class DetailPostView(generic.DetailView):
    model = foros_descrp
    template_name = 'foro/detailPost.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if (str(self.request.user.username) == str(self.object.creador)):
            context['isCreador'] = True
        else:
            context['isCreador'] = False
        return self.render_to_response(context)



class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = foros_descrp
    template_name = "foro/createPost.html"
    form_class = PostForm

    #def get_success_url(self):
    #    return reverse('foro:index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.creador = User.objects.get(username=self.request.user.username)
        post.save()
        return redirect('foro:index')

class ListPostsView(generic.ListView):
    model = foros_descrp
    template_name = 'foro/listPost.html'

class UpdatePostView(LoginRequiredMixin,generic.UpdateView):
    model = foros_descrp
    form_class = PostForm
    template_name = "foro/updatePost.html"


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if (str(self.request.user.username) == str(self.object.creador)):
            context['isCreador'] = True
        else:
            context['isCreador'] = False
        return self.render_to_response(context)


class DeletePostView(LoginRequiredMixin,generic.DeleteView):
    model = foros_descrp
    template_name = "foro/deletePost.html"
    def get_success_url(self):
        return reverse('foro:index')
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if (str(self.request.user.username) == str(self.object.creador)):
            context['isCreador'] = True
        else:
            context['isCreador'] = False
        return self.render_to_response(context)

class DenigedAcces(generic.TemplateView):
    template_name = 'foro/DenigedAcces.html'
