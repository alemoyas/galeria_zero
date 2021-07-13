from core.forms import AutorForm, ObraForm
from django.shortcuts import render, redirect  
from django.views.generic.detail import DetailView
from .models import Autor, Categoria, Obra
import random


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
        categorias = Categoria.objects.all()

        contexto = {'obra': obra,  'autor':autor, 'autores':autores, 'categorias':categorias}
        return render(request, 'core/ficha_obra.html', contexto)

def vista_dinamica_galeria(request, id):
        autores = Autor.objects.all()
        obras =   Obra.objects.filter(autor_id = id)
        autor = Autor.objects.get(idautor=id)
        categorias = Categoria.objects.all()

        contexto = {'obras': obras,  'autor':autor, 'autores':autores, 'categorias':categorias}
        return render(request, 'core/galeria_autor.html', contexto)

def vista_dinamica_autores(request, id):
        autores = Autor.objects.all()
        autor = Autor.objects.get(idautor=id)
        categorias = Categoria.objects.all()


        contexto = {'autor':autor, 'autores':autores, 'categorias':categorias}
        return render(request, 'core/ficha_autor.html', contexto)


def vista_dinamica_galeria_categoria(request, id):
        categorias = Categoria.objects.all()
        autores = Autor.objects.all()

        autores_match =  Autor.objects.filter(categoria_id = id)
        autor = Autor.objects.get(idautor=id)
        categoria = Categoria.objects.get(idcategoria=id)

        contexto = {'autores_match': autores_match,  'autor':autor, 'categoria':categoria, 'categorias':categorias, 'autores':autores}
        return render(request, 'core/galeria_categoria.html', contexto)


def index(request):

        autores = Autor.objects.all()
        categorias = Categoria.objects.all()

        obras_aleatorias = [random.choice(Obra.objects.filter(autor_id = random.choice(Autor.objects.filter(categoria_id = 2)))), 
        random.choice(Obra.objects.filter(autor_id = random.choice(Autor.objects.filter(categoria_id = 1)))), 
        random.choice(Obra.objects.filter(autor_id = random.choice(Autor.objects.filter(categoria_id = 4)))), 
        random.choice(Obra.objects.filter(autor_id = random.choice(Autor.objects.filter(categoria_id = 3))))]
        
        numeros = random.sample(list(Obra.objects.values_list('idobra', flat=True)), 3)
        numeros.sort()



        #filtra por muchas cosas, sirve!
        obras_carusel  = Obra.objects.filter(idobra__in=[numeros[0],numeros[1], numeros[2]]) 
        datos = {"autores" : autores, 'categorias':categorias, 'numeros':numeros, 'obras_carusel':obras_carusel, 'obras_aleatorias':obras_aleatorias}
        

        return render(request, "core/index.html", datos)



def navbar(request):
        categorias = Categoria.objects.all()
        autores = Autor.objects.all()
        datos = {"autores" : autores, 'categorias':categorias}
        return render(request, "core/navbar.html", datos)

def contacto(request):
        autores = Autor.objects.all()
        categorias = Categoria.objects.all()
        datos={'categorias':categorias, 'autores':autores}

        return render(request, "core/contacto.html", datos)

#Agregar Obra
def form_obra(request):

        categorias = Categoria.objects.all()
        autores = Autor.objects.all()

        data={'form':ObraForm, 'categorias':categorias, 'autores':autores}

        if request.method == 'POST':
                #recoge los datos
                formulario = ObraForm(data=request.POST, files=request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        data['mensaje'] = "Guardado Correctamente"

        return render(request,'core/form_obra.html',data)

#Modificar Obra
def form_mod_obra(request,id):
        autores = Autor.objects.all()
        categorias = Categoria.objects.all()

        obra = Obra.objects.get(idobra = id)
        data = {'form':ObraForm(instance=obra), 'autores':autores , 'categorias':categorias}

        if request.method == 'POST':
                formulario = ObraForm(data=request.POST, files=request.FILES, instance=obra)
                if formulario.is_valid():
                        formulario.save()
                        data['mensaje'] = "Modificado correctamente"
                        data['form'] = formulario        


        return render(request,'core/form_mod_obra.html',data)

def mod_obras(request):
        autores = Autor.objects.all()
        categorias = Categoria.objects.all()
        obras = Obra.objects.all()

        datos={"obras":obras , 'autores':autores, 'categorias':categorias}
        return render(request, "core/mod_obras.html", datos)


#Eliminar obra
def eliminar_obra(request, id):
        obra = Obra.objects.get(idobra = id)
        obra.delete()

        return redirect(to="mod_obras")

#Agregar autor
def form_autor(request):
        max_id = sorted(list(Autor.objects.values_list('idautor', flat=True)))[-1]
        categorias = Categoria.objects.all()
        obras = Obra.objects.all()
        autores = Autor.objects.all()

        data={'form':AutorForm, 'categorias':categorias, 'obras':obras, 'max_id':max_id, 'autores':autores}

        if request.method == 'POST':
                #recoge los datos
                formulario = AutorForm(data=request.POST, files=request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        data['mensaje'] = "Guardado Correctamente"

        return render(request,'core/form_autor.html',data)

#modificar autor
def form_mod_autor(request,id):
        autores = Autor.objects.all()
        obras = Obra.objects.all()
        categorias = Categoria.objects.all()

        autor = Autor.objects.get(idautor = id)
        data = {'form':AutorForm(instance=autor), 'obras':obras , 'categorias':categorias, 'autores':autores}

        if request.method == 'POST':
                formulario = AutorForm(data=request.POST, files=request.FILES, instance=autor)
                if formulario.is_valid():
                        formulario.save()
                        data['mensaje'] = "Modificado correctamente"
                        data['form'] = formulario        


        return render(request,'core/form_mod_obra.html',data)

def mod_autores(request):
        obras = Obra.objects.all()
        categorias = Categoria.objects.all()
        autores = Autor.objects.all()

        datos={"autores":autores , 'obras':obras, 'categorias':categorias}
        return render(request, "core/mod_autores.html", datos)

#Eliminar autor
def eliminar_autor(request, id):
        autor = Autor.objects.get(idautor = id)
        autor.delete()

        return redirect(to="mod_autores")

#vista modificar
def modificar(request):
        categorias = Categoria.objects.all()
        autores = Autor.objects.all()

        datos={"autores":autores , 'categorias':categorias}

        return render(request, "core/modificar.html", datos)

#vista agregar
def agregar(request):
        categorias = Categoria.objects.all()
        autores = Autor.objects.all()

        datos={"autores":autores , 'categorias':categorias}
        return render(request, "core/agregar.html", datos)

def chicago(request):
        obras = Obra.objects.all()
        categorias = Categoria.objects.all()
        return render(request, "core/chicagoGaleria.html")