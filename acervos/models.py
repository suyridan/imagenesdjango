from django.db import models

# Create your models here.
class Acervo(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)