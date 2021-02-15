from django.urls import path
#Views
from foro import views

urlpatterns = [
    path(
        route = '', 
        view = views.ListPostsView.as_view(), 
        name = 'index'
    ),
    path(
        route = 'foro/<int:pk>',
        view = views.DetailPostView.as_view(),
        name = 'detailPost'
    ),
    path(
        route = 'foro/crear', 
        view = views.CreatePostView.as_view(), 
        name = 'createPost'
    ),
]

