from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Autor, Obra


def prueba(request):

        #cosas de picasso
        picasso = Autor.objects.get(idautor=1)
        picasso_obras = [Obra.objects.get(idobra=1), Obra.objects.get(idobra=2), Obra.objects.get(idobra=3), Obra.objects.get(idobra=4)]


        #todos los autores todas las obras
        autores = Autor.objects.all()
        obras =   Obra.objects.all()


        datos = {"picasso" : picasso, "autores" : autores, "obras" : obras, "picasso_obras" : picasso_obras}
        
        

        return render(request, "core/prueba.html", datos)




def index(request):
        return render(request, "core/index.html")

def nadvar(request):
        return render(request, "core/nadvar.html")

def contacto(request):
        return render(request, "core/vistas_extras/contacto.html")


def galeria_picasso(request):
        o1 = Obra.objects.get(idobra=1)
        o2 = Obra.objects.get(idobra=2)
        o3 = Obra.objects.get(idobra=3)
        o4 = Obra.objects.get(idobra=4)
        
        datos = {"o1" :o1, "o2" :o2, "o3" :o3, "o4" :o4}
        return render(request, "core/galerias/galeria_picasso.html", datos)

        
def ficha_autorretrato_picasso(request):
        obra = Obra.objects.get(idobra=1)
        datos = {"obra" : obra}
        return render(request, "core/fichas/ficha_autorretrato_picasso.html",datos)

