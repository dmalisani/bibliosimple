from django.shortcuts import render
from .models import Libro
from dal import autocomplete

class LibroAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Libro.objects.none()

        qs = Libro.objects.all()

        if self.q:
            qs = qs.filter(titulo__icontains=self.q)

        return qs