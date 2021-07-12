from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Autor, Categoria, Obra


def prueba(request):

        #cosas de picasso
        picasso = Autor.objects.get(idautor=1)
        picasso_obras = Obra.objects.filter(autor_id = 1) #filtrar para objketido id

        #todos los autores todas las obras
        autores = Autor.objects.all()
        obras =   Obra.objects.all()

        datos = {"picasso" : picasso, "autores" : autores, "obras" : obras, "picasso_obras" : picasso_obras}
        

        return render(request, "core/prueba.html", datos)


def vista_dinamica_obras(request, id):
        autores = Autor.objects.all()
        obra = Obra.objects.get(idobra=id)
        autor = Autor.objects.get(idautor=Obra.objects.get(idobra=id).autor_id)

        contexto = {'obra': obra,  'autor':autor, 'autores':autores}
        return render(request, 'core/ficha_obra.html', contexto)

def vista_dinamica_galeria(request, id):
        autores = Autor.objects.all()
        obras =   Obra.objects.filter(autor_id = id)
        autor = Autor.objects.get(idautor=id)

        contexto = {'obras': obras,  'autor':autor, 'autores':autores}
        return render(request, 'core/galeria_autor.html', contexto)

def vista_dinamica_autores(request, id):
        autores = Autor.objects.all()
        autor = Autor.objects.get(idautor=id)


        contexto = {'autor':autor, 'autores':autores}
        return render(request, 'core/ficha_autor.html', contexto)


def vista_dinamica_galeria_categoria(request, id):

        autores =  Autor.objects.filter(categoria_id = id)
        autor = Autor.objects.get(idautor=id)
        categoria = Categoria.objects.get(idcategoria=id)

        contexto = {'autores': autores,  'autor':autor, 'categoria':categoria}
        return render(request, 'core/galeria_categoria.html', contexto)


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




