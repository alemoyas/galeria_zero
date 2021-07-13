from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls.static import static
from django.conf import settings
from .views import  prueba, index, navbar, contacto, vista_dinamica_autores, vista_dinamica_obras, vista_dinamica_galeria, vista_dinamica_galeria_categoria, form_obra, form_mod_obra, mod_obras, eliminar_obra



urlpatterns = [
    path('prueba/',prueba,name="prueba"),
    path('index/',index,name="index"),
    path('navbar/',navbar,name="navbar"),
    path('contacto/',contacto,name="contacto"),






    #paths dinamicos 
    path('obras/<int:id>',vista_dinamica_obras, name="obra"),
    path('autores/<int:id>',vista_dinamica_autores, name="autor"),
    path('galeria/<int:id>',vista_dinamica_galeria, name="galeria"),
    path('categoria/<int:id>',vista_dinamica_galeria_categoria, name="categoria"),



    #path crud
    path('form-obra/',form_obra,name="form_obra"),
    path('form-mod-obra/<id>',form_mod_obra,name="form_mod_obra"),
    path('mod-obras/',mod_obras,name="mod_obras"),
    path('eliminar-obra/<id>', eliminar_obra, name="eliminar_obra"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



