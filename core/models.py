from django.db import models

# Create your models here.

# Create your models here.

class Categoria(models.Model):
    idcategoria = models.IntegerField(primary_key=True,verbose_name="idcategoria")
    nombre = models.CharField(max_length=250,verbose_name="Nombre categoria")
    def __str__(self):
        return  self.nombre



class Autor(models.Model):
    idautor = models.IntegerField(primary_key=True,verbose_name="idautor")
    nombre = models.CharField(max_length=250,verbose_name="Nombre autor")
    historia = models.TextField(verbose_name="Historia")
    img = models.ImageField(upload_to='autores', null=True)
    categoria = models.ForeignKey(Categoria,default=1, on_delete=models.CASCADE)

    def __str__(self):
        return  self.nombre
        return  self.historia



class Obra(models.Model):
    idobra = models.IntegerField(primary_key=True,verbose_name="idobra")
    nombre = models.CharField(max_length=250,verbose_name="Nombre obra")
    historia = models.TextField(verbose_name="Historia")
    img = models.ImageField(upload_to='obras', null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    precio = models.IntegerField(verbose_name="precio",  default=0)
    fecha = models.IntegerField(verbose_name="anno",  default=0)

    def __str__(self):
        return  self.nombre
        return  self.historia


