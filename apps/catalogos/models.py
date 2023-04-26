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