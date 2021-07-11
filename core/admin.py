from django.contrib import admin
from .models import Autor, Obra 
from django.contrib import admin

class obraAdmin(admin.ModelAdmin):
    list_display = ('idobra', 'nombre', 'idautor')

class autorAdmin(admin.ModelAdmin):
    list_display = ('idautor', 'nombre')


admin.site.register(Autor, autorAdmin)
admin.site.register(Obra, obraAdmin)

