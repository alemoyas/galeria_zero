from django.contrib import admin
from .models import Autor, Obra 
from django.contrib import admin

class obraAdmin(admin.ModelAdmin):
    list_display = ('idobra', 'nombre', 'idautor')

admin.site.register(Autor)
admin.site.register(Obra, obraAdmin)

