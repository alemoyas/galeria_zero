from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls.static import static
from django.conf import settings

from .views import  prueba, index, nadvar, contacto, ficha_autorretrato_picasso, galeria_picasso



urlpatterns = [
    path('prueba/',prueba,name="prueba"),
    path('index/',index,name="index"),
    path('nadvar/',nadvar,name="nadvar"),
    path('contacto/',contacto,name="contacto"),
    path('ficha_autorretrato_picasso/',ficha_autorretrato_picasso,name="ficha_autorretrato_picasso"),
    path('galeria_picasso/',galeria_picasso,name="galeria_picasso")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



