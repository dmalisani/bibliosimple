from dal import autocomplete

from django.conf.urls import url


from .views import LibroAutocomplete

urlpatterns = [
    url(
        r'^libro-autocomplete/$',
        LibroAutocomplete.as_view(),
        name='libro-autocomplete',
    ),
]

