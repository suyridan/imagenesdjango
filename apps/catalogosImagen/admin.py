from django.contrib import admin
from .models import (Autor, Personaje, Editor, AutorTipo, FechaTipo, Epoca, Forma, ActorFuncion, Grupo, FotograficoProceso, 
                     GeneroFuncion, Tema, Subtema, RepografiaTecnica, RepografiaMateriales, Polaridad, Color, Orientacion, 
                     Portador, Tipo, HistoriaArchivisticaTipo, Original, GeneralDeterioro, ImagenDeterioro, EstructuralMenorDeterioro, EstructuralMayorDeterioro, ConservacionEstado, 
                     Cargo)
# Register your models here.
admin.site.register(Autor)

admin.site.register(Personaje)

admin.site.register(Editor)
    
admin.site.register(AutorTipo)
    
admin.site.register(FechaTipo)

admin.site.register(Epoca)
    
admin.site.register(Forma)

admin.site.register(ActorFuncion)
    
admin.site.register(Grupo)

admin.site.register(FotograficoProceso)

admin.site.register(GeneroFuncion)
    
admin.site.register(Tema)

admin.site.register(Subtema)

admin.site.register(RepografiaTecnica)
    
admin.site.register(RepografiaMateriales)

admin.site.register(Polaridad)
    
admin.site.register(Color)
    
admin.site.register(Orientacion)

admin.site.register(Portador)
    
admin.site.register(Tipo)

admin.site.register(HistoriaArchivisticaTipo)
    
admin.site.register(Original)
    
admin.site.register(GeneralDeterioro)

admin.site.register(ImagenDeterioro)
    
admin.site.register(EstructuralMenorDeterioro)
    
admin.site.register(EstructuralMayorDeterioro)

admin.site.register(ConservacionEstado)
    
admin.site.register(Cargo)