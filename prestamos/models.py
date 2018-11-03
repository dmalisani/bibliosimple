from django.db import models
from libros.models import Libro

class Lector(models.Model):
    """
    Persona físico registrada. Podrá retirar libros
    """
    nombre = models.CharField(max_length=100, verbose_name="Apellido y nombre")
    dni = models.CharField(max_length=11, unique=True, help_text="Por favor coloque los '.' en el nro de dni")
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    domicilio = models.CharField(max_length=50, blank=True, null=True)
    docente = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0} ({1})".format(self.nombre, self.dni)

    class Meta:
        verbose_name_plural = "Lectores"
        ordering = ["nombre",]


class Prestamo(models.Model):
    """
    Registra cada evento de préstamo de libros
    """
    fecha_prestamo = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Retiro")
    persona = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_devuelto = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Devolución")
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0} - {1}".format(self.fecha_prestamo.date().strftime("%d/%m/%Y"), self.libro)

    class Meta:
        ordering = ["fecha_prestamo",]






