from django.db import models


class Materia(models.Model):
    """
    Clasificación principal de los libros. Ejemplo MATEMÁTICA, FÍSICA
    """
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre",]

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.title()
        super(Materia, self).save(*args, **kwargs)

class Submateria(models.Model):
    """
    Clasificación específica de lo libros. Ejemplo MATEMÁTICA/CALCULO NUMÉRICO, FÍSICA/ÓPTICA
    """
    nombre = models.CharField(max_length=200)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)

    def __str__(self):
        return "{0} / {1}".format(self.materia.nombre, self.nombre)

    class Meta:
        ordering = ["materia__nombre", "nombre"]
        unique_together = ("nombre", "materia")

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.title()
        super(Submateria, self).save(*args, **kwargs)

class Editorial(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Editoriales"
        ordering = ["nombre",]

class Libro(models.Model):
    """
    Cada Libro físico es un registro, para eso se agrega un nro de ejemplar para identificarlos
    """
    submateria = models.ForeignKey(Submateria, on_delete=models.PROTECT, verbose_name='Materia')
    titulo = models.CharField(max_length=250)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    anno = models.CharField(max_length=4, blank=True, null=True, verbose_name="año", help_text="Año de edición")
    edicion = models.CharField(max_length=13, blank=True, null=True, verbose_name="Edición", help_text="Versión de edición")
    isbn = models.CharField(max_length=200)
    autor = models.CharField(max_length=250, help_text="Autor o autores (separados por , )")
    codigo = models.CharField(max_length=14, unique=True)
    _CHOICE_ESTADO = (('N','Nuevo'), ('U','Uso normal'), ('D', 'Deteriorado'), ('I', 'Inulitilzable'))
    estado = models.CharField(max_length=1, blank=True, null=True, choices=_CHOICE_ESTADO, default='U')
    nro_ejemplar = models.PositiveSmallIntegerField(default=1)
    baja = models.BooleanField(default=False)
    lengua_extranjera = models.BooleanField(default=False, verbose_name='Lengua extranjera', help_text='Escrito en otro idioma (sin traducir)')
    claves = models.TextField(blank=True, null=True, verbose_name="Claves de búsqueda", help_text="ciertas palabras que permitan encontrar el ejemplar")
    paginas = models.CharField(max_length=14, blank=True, null=True, verbose_name="Páginas")
    formato = models.CharField(max_length=14, blank=True, null=True, verbose_name="Formato", help_text="Alto y ancho en cm")
    observaciones = models.TextField(blank=True, null=True)


    def __str__(self):

        return "{0} {1}". format(self.titulo,  "("+str(self.nro_ejemplar) +"º ejemplar) " if self.nro_ejemplar > 1 else "")
        

    class Meta:
        ordering = ["titulo",]

