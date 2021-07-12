from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Autor, Obra


def prueba(request):

        #cosas de picasso
        picasso = Autor.objects.get(idautor=1)
        p1 = Obra.objects.get(idobra=1)
        p2 = Obra.objects.get(idobra=2)
        p3 = Obra.objects.get(idobra=3)
        p4 = Obra.objects.get(idobra=4)
        picasso_obras = [p1, p2, p3, p4]


        #todos los autores todas las obras
        autores = Autor.objects.all()
        obras =   Obra.objects.all()


        datos = {"picasso" : picasso, "autores" : autores, "obras" : obras, "p1" : p1, "picasso_obras" : picasso_obras}
        
        

        return render(request, "core/prueba.html", datos)




def index(request):
        return render(request, "core/index.html")

def nadvar(request):
        return render(request, "core/nadvar.html")
