from django.contrib import admin
from .models import Lector, Prestamo
from datetime import datetime
from .forms import PrestamoForm

class PrestamoAdmin(admin.ModelAdmin):
    class DevolucionListFilter(admin.SimpleListFilter):

        title = 'Estado'


        parameter_name = 'fecha_devuelto'

        def lookups(self, request, model_admin):

            return (
                ('SD', 'Sin devolución'),
                ('DV', 'Solo Devueltos'),
            )

        def queryset(self, request, queryset):

            if self.value() == 'SD':
                return queryset.filter(fecha_devuelto__isnull=True)
            if self.value() == 'DV':
                return queryset.filter(fecha_devuelto__isnull=False)

    def devolver(modeladmin, request, queryset):

        for pre in queryset:
            if not pre.fecha_devuelto:
                pre.fecha_devuelto = datetime.now()
                pre.save()

    devolver.short_description = "Marcar como devueltos los seleccionados"

    fields = ('persona', 'libro', 'observaciones', 'fecha_devuelto')
    list_display = ['__str__', 'persona', 'fecha_devuelto']
    #list_display_links = ['libro']
    search_fields = ['persona__nombre', 'libro__titulo']
    actions = [devolver]
    readonly_fields =  ['fecha_devuelto',]
    list_filter = [DevolucionListFilter,]
    form = PrestamoForm


admin.site.register(Lector)
admin.site.register(Prestamo, PrestamoAdmin)

