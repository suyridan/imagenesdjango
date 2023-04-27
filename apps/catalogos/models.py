from django.db import models
from treenode.models import TreeNodeModel

# Create your models here.    
class Ubicacion(TreeNodeModel): # los contenedores
    treenode_display_field = "nombre"
    
    nombre = models.CharField(max_length=200)
    nivel= models.IntegerField()
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    class Meta(TreeNodeModel.Meta):
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"
        
class Pais(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=10)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
    
class Estado(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=10)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Municipio(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=10)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
