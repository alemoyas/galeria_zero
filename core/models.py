from django.db import models

# Create your models here.

# Create your models here.
class Autor(models.Model):
    idautor = models.IntegerField(primary_key=True,verbose_name="idautor")
    nombre = models.CharField(max_length=250,verbose_name="Nombre autor")
    historia = models.TextField(verbose_name="Historia")
    img = models.ImageField(upload_to='autores', null=True)
    def __str__(self):
        return  self.nombre
        return  self.historia
        return  self.img


class Obra(models.Model):
    idobra = models.IntegerField(primary_key=True,verbose_name="idobra")
    nombre = models.CharField(max_length=250,verbose_name="Nombre obra")
    historia = models.TextField(verbose_name="Historia")
    img = models.ImageField(upload_to='obras', null=True)
    idautor  = models.ForeignKey(Autor, on_delete=models.CASCADE)


    def __str__(self):
        return  self.nombre
        return  self.historia


