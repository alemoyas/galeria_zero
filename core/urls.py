from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls.static import static
from django.conf import settings

from .views import  prueba, index, nadvar



urlpatterns = [
    path('prueba/',prueba,name="prueba"),
    path('index/',index,name="index"),
    path('nadvar/',nadvar,name="nadvar"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



