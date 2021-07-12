from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls.static import static
from django.conf import settings

from .views import  prueba, index, nadvar, contacto, vista_dinamica_autores, vista_dinamica_obras



urlpatterns = [
    path('prueba/',prueba,name="prueba"),
    path('',index,name="index"),
    path('nadvar/',nadvar,name="nadvar"),
    path('contacto/',contacto,name="contacto"),






    #paths dinamicos 
    path('obras/<int:id>',vista_dinamica_obras, name="obra"),
    path('autores/<int:id>',vista_dinamica_autores, name="autor")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



