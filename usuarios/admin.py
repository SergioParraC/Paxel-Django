from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
#Modelos
from django.contrib.auth.models import User
from usuarios.models import Perfil

# Register your models here.
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
    
admin.site.unregister(Perfil)
admin.site.register(Perfil, PerfilAdmin)