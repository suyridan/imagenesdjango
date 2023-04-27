from django.contrib import admin
from .models import Acervo, VisualImagen, FisicaImagen, Reprografia, ArchivistaHistoria, Contenedor
from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm

# Register your models here.
# admin.site.register(Acervo)
admin.site.register(VisualImagen)
admin.site.register(Acervo)
admin.site.register(FisicaImagen)
admin.site.register(Reprografia)
admin.site.register(ArchivistaHistoria)


@admin.register(Contenedor)
class AcervoAdmin(TreeNodeModelAdmin):

    # set the changelist display mode: 'accordion', 'breadcrumbs' or 'indentation' (default)
    # when changelist results are filtered by a querystring,
    # 'breadcrumbs' mode will be used (to preserve data display integrity)
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_BREADCRUMBS
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_INDENTATION

    # use TreeNodeForm to automatically exclude invalid parent choices
    form = TreeNodeForm