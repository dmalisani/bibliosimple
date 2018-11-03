from django.conf.urls import url
from dal import autocomplete

from .views import LectorAutocomplete

urlpatterns = [
    url(
        r'^lector-autocomplete/$',
        LectorAutocomplete.as_view(),
        name='lector-autocomplete',
    ),
]