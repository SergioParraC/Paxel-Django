from django.urls import path
#Views
from foro import views

urlpatterns = [
    path(
        route = 'inicio/', 
        view = views.inicio_view, 
        name = 'inicio'
    ),
]

