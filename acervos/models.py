from django.db import models

class Acervo(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return ' - ' + self.nombre

class VisualImagen(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    acervo = models.ForeignKey(Acervo, on_delete=models.CASCADE)
    
class FisicaImagen(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    visual = models.ForeignKey(VisualImagen, on_delete=models.CASCADE)

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