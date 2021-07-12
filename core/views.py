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


def vista_dinamica(request, id):
        obra = Obra.objects.get(idobra=id)
        idautor = Obra.objects.get(idobra=id).autor_id
        autor = Autor.objects.get(idautor=idautor)

        contexto = {'obra': obra, 'idautor' : idautor, 'autor':autor}
        return render(request, 'core/ficha_obra.html', contexto)



def index(request):
        return render(request, "core/index.html")

def nadvar(request):
        return render(request, "core/nadvar.html")

def contacto(request):
        return render(request, "core/vistas_extras/contacto.html")




def galeria_picasso(request):
        

        
        return render(request, "core/galerias/galeria_picasso.html", )

