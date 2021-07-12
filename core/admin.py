from django.contrib import admin
from .models import Autor, Obra, Categoria
from django.contrib import admin

class obraAdmin(admin.ModelAdmin):
    list_display = ('idobra', 'nombre', 'autor')

class autorAdmin(admin.ModelAdmin):
    list_display = ('idautor', 'nombre', 'categoria')

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('idcategoria', 'nombre')


admin.site.register(Autor, autorAdmin)
admin.site.register(Obra, obraAdmin)
admin.site.register(Categoria, categoriaAdmin)

