from django.urls import path
#Views
from foro import views

urlpatterns = [
    path(
        #Lista los post
        route = '', 
        view = views.ListPostsView.as_view(), 
        name = 'index'
    ),
    path(
        #Detalle del post
        route = 'foro/<int:pk>',
        view = views.DetailPostView.as_view(),
        name = 'detailPost'
    ),
    path(
        #Crear un post
        route = 'foro/crear', 
        view = views.CreatePostView.as_view(), 
        name = 'createPost'
    ),
    path(
        #Actualizar un post
        route = 'foro/edit/<int:pk>',
        view = views.UpdatePostView.as_view(),
        name = 'updatePost'
    ),
    path(
        #Eliminar un post
        route = 'foro/delete/<int:pk>',
        view = views.DeletePostView.as_view(),
        name = 'deletePost'
    ),
    
]

