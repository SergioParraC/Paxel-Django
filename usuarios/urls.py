from django.urls import path
#Views
from usuarios import views

urlpatterns = [
    path(
        route = 'login/', 
        view = views.login_view, 
        name = 'login'
    ),
    path(
        route = 'logout/',
        view = views.logout_view,
        name = 'logout'
    ),
    path(
        route = 'signup/',
        view = views.crear_usuario,
        name = 'crear_usuario',
    ),
    path(
        route = 'update/',
        view = views.act_datos_view,
        name = 'act_datos',
    ),
]

