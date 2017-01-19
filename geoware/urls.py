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
    url(
        r'^timezone/autocomplete/$',
        TimezoneAutocompleteView.as_view(),
        name='timezone-autocomplete',
    ),
    url(
        r'^altnames/autocomplete/$',
        AltnameAutocompleteView.as_view(),
        name='altnames-autocomplete',
    ),
    url(
        r'^currency/autocomplete/$',
        CurrencyAutocompleteView.as_view(),
        name='currency-autocomplete',
    ),
    url(
        r'^language/autocomplete/$',
        LanguageAutocompleteView.as_view(),
        name='language-autocomplete',
    ),
]
