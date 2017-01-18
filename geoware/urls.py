from django.conf.urls import url

from dal import autocomplete

from .views import *

urlpatterns = [
    url(
        r'^country/autocomplete/$',
        CountryAutocompleteView.as_view(),
        name='country-autocomplete',
    ),
    url(
        r'^division/autocomplete/$',
        DivisionAutocompleteView.as_view(),
        name='division-autocomplete',
    ),
    url(
        r'^subdivision/autocomplete/$',
        SubdivisionAutocompleteView.as_view(),
        name='subdivision-autocomplete',
    ),
    url(
        r'^city/autocomplete/$',
        CityAutocompleteView.as_view(),
        name='city-autocomplete',
    ),
]
