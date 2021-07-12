from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Autor, Obra


def prueba(request):
        picasso = Autor.objects.get(idautor=1)
        
        autores = Autor.objects.all()
        obras =   Obra.objects.all()


        datos = {"picasso" : picasso, "autores" : autores, "obras" : obras}
        
        

        return render(request, "core/prueba.html", datos)


class prueba(DetailView):
        obras =   Obra.objects.all()
        model = obras 
        context_object_name = "obras"
        template_name = "core/prueba.html"



def index(request):
        return render(request, "core/index.html")

def nadvar(request):
        return render(request, "core/nadvar.html")
