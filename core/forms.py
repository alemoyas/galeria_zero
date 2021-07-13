from django.db.models import fields
from django.forms import ModelForm
from .models import Categoria, Obra, Autor

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['idobra','nombre','historia','img','autor','precio','fecha']


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['idautor', 'nombre', 'historia', 'img', 'categoria']