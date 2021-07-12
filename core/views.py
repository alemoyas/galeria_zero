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


def vista_dinamica_obras(request, id):
        obra = Obra.objects.get(idobra=id)
        autor = Autor.objects.get(idautor=Obra.objects.get(idobra=id).autor_id)

        contexto = {'obra': obra,  'autor':autor}
        return render(request, 'core/ficha_obra.html', contexto)

def vista_dinamica_autores(request, id):
        autor = Autor.objects.get(idautor=id)


        contexto = {'autor':autor}
        return render(request, 'core/ficha_autor.html', contexto)


def index(request):
        autores = Autor.objects.all()


        datos = {"autores" : autores}
        
        return render(request, "core/index.html", datos)




def navbar(request):
        autores = Autor.objects.all()
        datos = {"autores" : autores}
        return render(request, "core/navbar.html", datos)

def contacto(request):
        return render(request, "core/vistas_extras/contacto.html")




