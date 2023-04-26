from django.db import models
from treenode.models import TreeNodeModel

class Contenedor(TreeNodeModel): # los contenedores
    treenode_display_field = "nombre"
    
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    class Meta(TreeNodeModel.Meta):
        verbose_name = "Contenedor"
        verbose_name_plural = "Contenedores"

class Acervo(models.Model): # el cliente, relacionado a los usuarios
    name=models.CharField(max_length=255)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.name

class LicenciaTipo(models.Model): # tipos de permisos
    name=models.CharField(max_length=255)
    estatus=models.BooleanField(default=True)
    
    
    
    
class Imagen(models.Model):
    titulo = models.CharField(max_length=255)
    estatus = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    acervo = models.ForeignKey(Acervo, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.titulo
    class Meta:
        abstract = True
    
    
class VisualImagen(Imagen):
    ubicacion=models.ForeignKey("catalogos.Ubicacion", related_name='imagenes', on_delete=models.CASCADE)
    titulo_origen = models.CharField(max_length=255)
    
class FisicaImagen(Imagen):
    contenedor = models.ForeignKey(Contenedor, on_delete=models.CASCADE)

class Licencia(models.Model): # Permisos por cliente 1 - M 
    vigencia = models.DateTimeField(auto_now_add=True)
    tipo_licencia = models.ForeignKey(LicenciaTipo, on_delete=models.CASCADE)
    Acervo=models.ForeignKey(Acervo, on_delete=models.CASCADE)
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