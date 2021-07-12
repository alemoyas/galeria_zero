from django.db.models import fields
from django.forms import ModelForm
from .models import Obra

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['idobra','nombre','historia','img','autor','precio','fecha']

