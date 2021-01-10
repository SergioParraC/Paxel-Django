from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
#Modelos
from django.contrib.auth.models import User
from usuarios.models import Perfil
from foro.models import foros_descrp

#Admin de usuarios
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nick','sentecia','pais','nacim')
    search_fields = ('nick',)
    
    fieldsets = (
        ('Basico', {
            "fields": (
                ('nick',),
                ('creado','pais','num_celular',)
            ),
        }),
        ('Administrador:', {
            "fields": (
                ('sentecia',)
            )
        }),
    )
    readonly_fields = ('nick','imagen','creado','nacim','num_celular','pais','biografia',)
    
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfil'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)
    
#Admin de Foros
class ForosAdmin(admin.ModelAdmin):
    list_display = ('titulo','id_foro','solicitud_moderacion','resumen')
    fieldsets = (
        ('Basico', {
            "fields": (
                ('titulo','nick','videojuego'),
                ('codigo_foro','fecha_creacion','consola'),
            ),
        }),
        ('Moderacion de contenido', {
            'fields': (
                ('solicitud_moderacion'),
            ),
        }),
        ('contenido',{
            'fields': (
                ('resumen'),
                ('imagen'),
                ('contenido'),
            ),
        })
    )
    
    readonly_fields = ('fecha_creacion','titulo','videojuego','resumen','contenido','consola','id_foro','imagen')
admin.site.register(foros_descrp, ForosAdmin)
admin.site.unregister(Perfil)
admin.site.register(Perfil, PerfilAdmin)

