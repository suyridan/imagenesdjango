from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class Personaje(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class Editor(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class AutorTipo(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class FechaTipo(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class Epoca(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class Forma(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class Rol(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class ActorFuncion(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class Grupo(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class FotograficoProceso(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
# class EditorColeccionista(models.Model):
#     nombre = models.CharField(max_length=200)
#     estatus = models.BooleanField()
#     created_at = models.DateTimeField(auto_now=True)

class GeneroFuncion(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class Tema(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class Subtema(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    tema = models.ForeignKey( Tema, on_delete=models.CASCADE)
    
# class Descriptor(models.Model):
#     nombre = models.CharField(max_length=200)
#     estatus = models.BooleanField()
#     created_at = models.DateTimeField(auto_now=True)

class RepografiaTecnica(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class RepografiaMateriales(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class Polaridad(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class Color(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class Orientacion(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class Portador(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class Tipo(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class HistoriaArchivisticaTipo(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class Original(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class GeneralDeterioro(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class ImagenDeterioro(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class EstructuralMenorDeterioro(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class EstructuralMayorDeterioro(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

class ConservacionEstado(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
class Cargo(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)