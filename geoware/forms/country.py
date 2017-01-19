from django import forms
from django.utils.translation import ugettext as _

from dal import autocomplete
from dal import forward

from ..models import Country


class CountryForm(forms.ModelForm):
    """
    Custom Country Form.
    """
    class Meta:
        model = Country
        fields = ('__all__')
        widgets = {
            'jurisdiction': autocomplete.ModelSelect2(
                url='geoware:country-autocomplete',
                attrs={
                    'data-placeholder': _('LOCATION.COUNTRY.JURISDICTION'),
                    'data-minimum-input-length': 0,
                }
            ),
            'currency': autocomplete.ModelSelect2(
                url='geoware:currency-autocomplete',
                attrs={
                    'data-placeholder': _('LOCATION.CURRENCY'),
                    'data-minimum-input-length': 0,
                }
            ),
            'capital': autocomplete.ModelSelect2(
                url='geoware:city-autocomplete',
                forward=[forward.Field(src="jurisdiction", dst="country"), ],
                attrs={
                    'data-placeholder': _('LOCATION.CAPITAL'),
                    'data-minimum-input-length': 0,
                }
            ),
        }
