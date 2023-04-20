from django.db import models
from treenode.models import TreeNodeModel

class Acervo(TreeNodeModel): # los contenedores
    treenode_display_field = "nombre"
    
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    class Meta(TreeNodeModel.Meta):
        verbose_name = "Acervo"
        verbose_name_plural = "Acervos"

class AcervoCliente(models.Model): # el cliente, relacionado a los usuarios
    name=models.TextField(max_length=255)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class LicenciaTipo(models.Model): # tipos de permisos
    name=models.TextField(max_length=255)
    estatus=models.BooleanField(default=True)
    
    
    
    
class Imagen(models.Model):
    titulo = models.CharField(max_length=255)
    estatus = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
    
    
class VisualImagen(Imagen):
    acervo = models.ForeignKey(Acervo, on_delete=models.CASCADE)
    
class FisicaImagen(Imagen):
    contenedor = models.ForeignKey(Acervo, on_delete=models.CASCADE)

class Licencia(models.Model): # Permisos por cliente 1 - M 
    vigencia = models.DateTimeField(auto_now_add=True)
    tipo_licencia = models.ForeignKey(LicenciaTipo, on_delete=models.CASCADE)
    AcervoCliente=models.ForeignKey(AcervoCliente, on_delete=models.CASCADE)
    VisualImagenes=models.ManyToManyField(VisualImagen)



class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class Personaje(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class Reprografia(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class Editor(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class ArchivistaHistoria(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    fisica = models.ForeignKey(FisicaImagen, on_delete=models.CASCADE)