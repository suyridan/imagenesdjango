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
    ubicacion=models.ForeignKey("catalogos.Ubicacion", on_delete=models.CASCADE)
    titulo_origen = models.CharField(max_length=255)
    ruta_imagen = models.CharField(max_length=5000)
    titulo_atribuido = models.CharField()
    titulo_otro_idioma = models.CharField()
    rasgo_distintivo = models.CharField()
    autoria_atribuida = models.CharField()
    fecha_año = models.SmallIntegerField()
    fecha_dia = models.SmallIntegerField()
    fecha_mes = models.SmallIntegerField()
    fecha_tipo = models.ForeignKey("catalogosImagen.FechaTipo", on_delete=models.CASCADE)
    pais=models.ForeignKey("catalogos.Pais", on_delete=models.CASCADE)
    estado=models.ForeignKey("catalogos.Estado", on_delete=models.CASCADE)
    municipio=models.ForeignKey("catalogos.Municipio", on_delete=models.CASCADE)
    informacion_adicional = models.TextField()
    lugar = models.CharField()
    rol = models.ForeignKey("catalogosImagen.Rol", on_delete=models.CASCADE)
    epoca = models.ForeignKey("catalogosImagen.Epoca", on_delete=models.CASCADE)
    funcion_o_genero = models.CharField()
    grupo = models.ForeignKey("catalogosImagen.Grupo", on_delete=models.CASCADE)
    tema = models.ForeignKey("catalogosImagen.Tema", on_delete=models.CASCADE)
    subtema = models.ForeignKey("catalogosImagen.Subtema", on_delete=models.CASCADE)
    reprografia = models.CharField()
    obra_repografiada = models.CharField()
    
    class Meta():
        verbose_name = "Imagen Visual"
        verbose_name_plural = "Imagenes Visuales"
        

    
class FisicaImagen(Imagen):
    contenedor = models.ForeignKey(Contenedor, on_delete=models.CASCADE)

class Reprografia(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class ArchivistaHistoria(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    fisica = models.ForeignKey(FisicaImagen, on_delete=models.CASCADE)