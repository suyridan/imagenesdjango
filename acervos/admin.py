from django.contrib import admin
from .models import Acervo, VisualImagen, FisicaImagen, Autor, Reprografia, ArchivistaHistoria, Personaje, Editor

# Register your models here.
admin.site.register(Acervo)
admin.site.register(VisualImagen)
admin.site.register(FisicaImagen)
admin.site.register(Autor)
admin.site.register(Reprografia)
admin.site.register(ArchivistaHistoria)
admin.site.register(Personaje)
admin.site.register(Editor)
