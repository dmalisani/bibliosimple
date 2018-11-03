from django.contrib import admin
from .models import Libro, Editorial, Materia, Submateria
from django.contrib import messages



class EditorialAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
    search_fields = ['nombre',]

class MateriaAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
    search_fields = ['nombre',]

class LibroAdmin(admin.ModelAdmin):
    ordering = ('titulo',)
    list_display = ['__str__', 'submateria', 'autor', 'editorial',  'isbn']
    search_fields = ['titulo', 'autor', 'codigo', 'isbn', 'claves']
    list_filter = ('submateria__materia__nombre', 'editorial__nombre')


admin.site.register(Libro, LibroAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Submateria)


