from django.shortcuts import render
from .models import Lector
from dal import autocomplete

class LectorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Lector.objects.none()

        qs = Lector.objects.all()

        if self.q:
            qs = qs.filter(nombre__icontains=self.q)

        return qs